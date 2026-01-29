import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
import os
import warnings
warnings.filterwarnings('ignore')


# =============================================================================
# PCA COMPLETO CON ANOTACIONES INTERPRETABLES
# =============================================================================

def analisis_pca_completo():

    # -------------------------------------------------------------------------
    def cargar_archivo():
        while True:
            nombre = input("Ingrese el archivo (Excel o CSV): ").strip()

            if not os.path.exists(nombre):
                print("❌ No encontrado")
                continue

            return pd.read_csv(nombre) if nombre.endswith(".csv") else pd.read_excel(nombre)


    # -------------------------------------------------------------------------
    def procesar_ordinales(df):
        entrada = input("\nColumnas ordinales (coma) o Enter: ").strip()
        if not entrada:
            return df

        enc = OrdinalEncoder()
        for col in [c.strip() for c in entrada.split(",")]:
            df[col] = enc.fit_transform(df[[col]])
            print(f"  ✅ {col}")

        return df


    # -------------------------------------------------------------------------
    def procesar_nominales(df):
        entrada = input("\nColumnas nominales (coma) o Enter: ").strip()
        if not entrada:
            return df

        enc = OneHotEncoder(drop='first', sparse_output=False)

        for col in [c.strip() for c in entrada.split(",")]:
            dummy = enc.fit_transform(df[[col]])
            cats = enc.categories_[0][1:]
            new_cols = [f"{col}_{c}" for c in cats]

            df = pd.concat([df.drop(columns=[col]),
                            pd.DataFrame(dummy, columns=new_cols, index=df.index)], axis=1)

            print(f"  ✅ {col} → {len(new_cols)} dummies")

        return df


    # -------------------------------------------------------------------------
    def estandarizar(df):
        scaler = StandardScaler()
        df[df.columns] = scaler.fit_transform(df)
        print("✅ Estandarizadas")
        return df


    # -------------------------------------------------------------------------
    def pca_manual(df):

        corr = df.corr()
        eigval, eigvec = np.linalg.eigh(corr)

        idx = np.argsort(eigval)[::-1]
        eigval, eigvec = eigval[idx], eigvec[:, idx]

        var_exp = eigval / eigval.sum() * 100
        componentes = df.values @ eigvec

        return eigval, eigvec, var_exp, componentes, df.columns


    # -------------------------------------------------------------------------
    # 🔥 GRÁFICAS CON INTERPRETACIÓN
    # -------------------------------------------------------------------------
    def graficar(var_exp, componentes, cargas, nombres, eigval):

        sns.set_theme(style="whitegrid")

        # =====================================================
        # 1 Scree + Biplot
        # =====================================================
        fig, ax = plt.subplots(1, 2, figsize=(13, 5))

        # Scree
        ax[0].plot(var_exp, marker='o')

        # Kaiser rule
        kaiser = np.sum(eigval > 1)
        ax[0].axvline(kaiser-1, linestyle="--")
        ax[0].set_title("Scree Plot")
        ax[0].set_ylabel("Varianza (%)")

        ax[0].text(kaiser-1, max(var_exp)*0.8,
                   f"Kaiser ≈ {kaiser} PCs",
                   color="black")

        # Biplot
        pc1, pc2 = componentes[:, 0], componentes[:, 1]
        ax[1].scatter(pc1, pc2, alpha=0.6)

        scale = 1 / np.max(np.abs(cargas[:, :2]))

        for i, name in enumerate(nombres):
            ax[1].arrow(0, 0,
                        cargas[i, 0]*scale,
                        cargas[i, 1]*scale,
                        alpha=0.8)
            ax[1].text(cargas[i, 0]*scale,
                       cargas[i, 1]*scale,
                       name,
                       fontsize=9)

        ax[1].axhline(0)
        ax[1].axvline(0)
        ax[1].set_title("Biplot (variables + muestras)")

        plt.tight_layout()
        plt.savefig("pca_scree_biplot.png", dpi=300)
        plt.close()


        # =====================================================
        # 2 Varianza acumulada
        # =====================================================
        var_acum = np.cumsum(var_exp)
        n80 = np.argmax(var_acum >= 80) + 1

        plt.figure(figsize=(6,4))
        plt.plot(var_acum, marker='o')
        plt.axhline(80, linestyle='--')
        plt.axvline(n80-1, linestyle='--')

        plt.text(n80-1, 50,
                 f"{n80} PCs → {var_acum[n80-1]:.1f}%",
                 bbox=dict(facecolor='white'))

        plt.xlabel("Componentes")
        plt.ylabel("Varianza acumulada (%)")
        plt.title("Varianza acumulada")

        plt.savefig("varianza_acumulada.png", dpi=300)
        plt.close()


        # =====================================================
        # 3 Heatmap cargas
        # =====================================================
        plt.figure(figsize=(8,6))
        sns.heatmap(cargas[:, :4],
                    annot=True,
                    cmap="coolwarm",
                    center=0,
                    xticklabels=[f"PC{i+1}" for i in range(4)],
                    yticklabels=nombres)

        plt.title("Loadings\nValores altos = mayor influencia")
        plt.savefig("heatmap_cargas.png", dpi=300)
        plt.close()


        # =====================================================
        # 4 Scatter PC1-PC2
        # =====================================================
        plt.figure(figsize=(6,5))
        plt.scatter(pc1, pc2, alpha=0.7)

        plt.axhline(0)
        plt.axvline(0)

        plt.text(0.02, 0.95,
                 "Separación de muestras",
                 transform=plt.gca().transAxes)

        plt.xlabel("PC1")
        plt.ylabel("PC2")
        plt.title("Distribución de observaciones")

        plt.savefig("pc1_pc2_scatter.png", dpi=300)
        plt.close()


        # =====================================================
        # 5 Contribución PC1 (TOP variables)
        # =====================================================
        contrib = np.abs(cargas[:, 0])
        order = np.argsort(contrib)[::-1]

        plt.figure(figsize=(8,4))
        sns.barplot(x=list(nombres), y=contrib)

        top3 = order[:3]
        for i in top3:
            plt.text(i, contrib[i], "TOP", ha='center', va='bottom')

        plt.xticks(rotation=45)
        plt.title("Contribución a PC1\n(TOP = más influyentes)")

        plt.savefig("contribucion_pc1.png", dpi=300)
        plt.close()

        print("\n✅ Todas las gráficas guardadas correctamente")


    # ================= EJECUCIÓN =================

    df = cargar_archivo()
    df = procesar_ordinales(df)
    df = procesar_nominales(df)
    df = estandarizar(df)

    eigval, eigvec, var_exp, comp, nombres = pca_manual(df)
    cargas = eigvec * np.sqrt(eigval)

    graficar(var_exp, comp, cargas, nombres, eigval)


# =============================================================================

if __name__ == "__main__":
    analisis_pca_completo()
