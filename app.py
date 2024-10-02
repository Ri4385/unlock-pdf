import streamlit as st
import pikepdf

st.title("PDFパスワード解除アプリ")

uploaded_file = st.file_uploader("パスワード付きPDFをアップロード", type=["pdf"])
password = st.text_input("パスワードを入力", type="password")

if st.button("解除"):
    if uploaded_file and password:
        try:
            with pikepdf.open(uploaded_file, password=password) as pdf:
                output_file = "unlocked_pdf.pdf"
                pdf.save(output_file)

            st.success("PDFのパスワードが解除されました！ダウンロードしてください。")
            st.download_button("ダウンロード", data=open(output_file, "rb"), file_name=output_file)
        except pikepdf.PasswordError:
            st.error("パスワードが正しくありません。")
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
if st.button("パスワードを入力せずに解除"):
    if uploaded_file:
        password = "PhysChem24_SITT"
        try:
            with pikepdf.open(uploaded_file, password=password) as pdf:
                output_file = "unlocked_pdf.pdf"
                pdf.save(output_file)

            st.success("PDFのパスワードが解除されました！ダウンロードしてください。")
            st.download_button("ダウンロード", data=open(output_file, "rb"), file_name=output_file)
        except pikepdf.PasswordError:
            st.error("パスワードが正しくありません。")
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
            
