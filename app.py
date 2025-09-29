import streamlit as st;
import google.generativeai as genai 

GOOGLE_API_KEY = 'AIzaSyBoShzvepGFwmaB34-eGSBH3kdupx_IW2M'
genai.configure(api_key=GOOGLE_API_KEY)

for model in genai.list_models():
    print(model.name)
model = genai.GenerativeModel("gemini-2.5-pro")
def main():
    st.set_page_config(page_title="Sql Query Generator 🤖",page_icon=':robot:')
    st.markdown(
        """
            <div style = "text-align: center;">
                <h1>SQL Query Generator ⚙️ 🤖 📚</h1>
                <h3>I can Generate SQL Queries for you!!</h3>
                <h4>With Explanation as well !!!</h4>
                <p>This tool is a simple tool that allows you to generate SQL queries based on your prompts.</p>
            </div>
        """,
        unsafe_allow_html=True
    )

    text_input = st.text_area("Enter your Query here in Plain English : ")
    submit = st.button("Generate SQL Query")

    if submit:
        with st.spinner("Generating SQL Queries"):
            template = """
                Create a SQL Query snippet using below text:

                ```
                    {text_input}
                ```
                I just want SQL Query.
            """
            formatted_text = template.format(text_input=text_input)
            response = model.generate_content(formatted_text)
            sql_query = response.text
            sql_query = sql_query.strip().lstrip("```sql").rstrip('```')
            expected_output_template = """
                What would be the expected response of this SQL query snippet:

                ```
                    {sql_query}
                ```
                Provide sample tabular Response with no explanation.
            """
            expected_output_formatted = expected_output_template.format(sql_query=sql_query)
            expected_output = model.generate_content(expected_output_formatted)

            explanation = """
                Explain this SQL Query:

                ```
                    {sql_query}
                ```
                Please Provide with simplest explanation.
            """

            explanation_formatted = explanation.format(sql_query=sql_query)
            explanation_output = model.generate_content(explanation_formatted)

            with st.container():
                st.success("SQL Query Generated Successfully! Here is your Query Below : ")
                st.code(sql_query,language='sql')
                st.success("Expected ouput of this Query will be : ")
                st.markdown(expected_output.text)
                st.success("Explanation of this Query : ")
                st.markdown(explanation_output.text)


main()