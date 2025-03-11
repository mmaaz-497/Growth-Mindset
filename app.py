# # imports

# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO


# st.set_page_config(page_title="Data Sweeper", layout="wide")
# st.title("Data Sweeper")
# st.write("Transform yours files between CSV Excel formats with built-in data cleaning and visualization")
# uploaded_files = st.file_uploader("Upload you files(CSV or Excel):",type=["csv", "xlsx"], accept_multiple_files=True)

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()


#         if file_ext == ".csv":
#             df = pd.read_csv(file)
#         elif file_ext  == ".xlsx":
#             df = pd.read_excel(file)
#         else:
#             st.error(f"Unsupported file type: {file_ext}")
#             continue

#         #Display info about the file
#         st.write(f"**File Name:** {file.name}")
#         st.write(f"**File Size:** {file.size/1024}")

#         #show 5 some rows of data
#         st.write("Preview the Head of the Dataframe")
#         st.dataframe(df.head())

#         # options for data cleaning

#         st.subheader("Data Cleaning Option")
#         if st.checkbox(f"Clean Data for {file.name}"):
#             col1, col2 = st.columns(2)

#             with col1:
#                 if st.button(f"Remove duplicates from {file.name}") :
#                     df.drop_duplicates(inplace=True)
#                     st.write("Duplicates removed!")

#             with col2:
#                         if st.button(f"Fill missing values for {file.name}"):
#                             numeric_cols =df.select_dtypes(include="number").columns
#                             df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#                             st.write("Missing Values have been Filled!")


#         #Choose specific colums to keep or convert

#         st.subheader("Select colums to convert")
#         columns = st.multiselect(F"choose columns for {file.name}", df.columns, default=df.columns)
#         df = df[columns]


#         #Create some visualization
#         st.subheader("Data Visualization")
#         if st.checkbox(f"Show Visualization for {file.name}"):
#             st.bar_chart(df.select_dtypes(include="number").iloc[:,:2])


#             # convert the file ->CSV to Excel
#             st.subheader("Conversion option")
#             conversion_type = st.radio(f"convert {file.name} to:",["CSV", "Excel"], key=file.name)
#             if st.button(f"convert {file.name}"):
#                 buffer = BytesIO()
#             if conversion_type == "CSV":
#                 df.to_csv(buffer ,index=False)
#                 file_name = file.name.replace(file_ext,".csv")
#                 mime_type = "text/csv"

#             elif conversion_type == "Excel":
#                 df.to_excel(buffer , index=False)
#                 file_name = file_name.replace(file_ext,".xlsx")
#                 mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#             buffer.seek(0)
        
#         # Download Button
#         st.download_button(
#             label=f":download button: Download {file.name} as {conversion_type}",
#             data= buffer,
#             file_name= "file_name",
#             mime=mime_type
#         )
# st.success("All files processed!")




import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="🧹 Data Sweeper", layout="wide")
st.title("🧹 Data Sweeper")
st.write("✨ Transform your files between **CSV** and **Excel** formats with built-in data cleaning and visualization. 📊")

# File uploader
uploaded_files = st.file_uploader("📂 **Upload your files (CSV or Excel):**", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read the file into a DataFrame
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"❌ Unsupported file type: {file_ext}")
            continue

        # Display file info
        st.write(f"📄 **File Name:** `{file.name}`")
        st.write(f"📏 **File Size:** `{file.size / 1024:.2f} KB`")

        # Show preview of data
        st.write("🔍 **Preview of the DataFrame**")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader("🛠️ Data Cleaning Options")
        if st.checkbox(f"🧹 **Clean Data for `{file.name}`**"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"🗑️ Remove duplicates from `{file.name}`"):
                    df.drop_duplicates(inplace=True)
                    st.success("✅ Duplicates removed!")

            with col2:
                if st.button(f"🩹 Fill missing values for `{file.name}`"):
                    numeric_cols = df.select_dtypes(include="number").columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("✅ Missing values filled with column mean!")

        # Column selection for conversion
        st.subheader("📌 Select Columns to Keep")
        selected_columns = st.multiselect(f"🎯 Choose columns for `{file.name}`", df.columns, default=df.columns)
        df = df[selected_columns]

        # Data Visualization
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"📈 Show Visualization for `{file.name}`"):
            numeric_df = df.select_dtypes(include="number")
            if not numeric_df.empty:
                st.bar_chart(numeric_df.iloc[:, :2])
            else:
                st.warning("⚠️ No numerical data available for visualization.")

        # File Conversion Options
        st.subheader("🔄 Conversion Options")
        conversion_type = st.radio(f"🔃 Convert `{file.name}` to:", ["📄 CSV", "📊 Excel"], key=file.name)

        if st.button(f"⚡ Convert `{file.name}`"):
            buffer = BytesIO()
            
            if conversion_type == "📄 CSV":
                df.to_csv(buffer, index=False)
                new_file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "📊 Excel":
                df.to_excel(buffer, index=False, engine='openpyxl')
                new_file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            
            buffer.seek(0)

            # Download Button
            st.download_button(
                label=f"⬇️ Download `{new_file_name}`",
                data=buffer,
                file_name=new_file_name,
                mime=mime_type
            )

st.success("🎉 All files processed successfully!")

