# Natural Language to SQL Query Generator — Gemini Pro

Live demo: https://sql-query-generator-using-gemini.streamlit.app

## Project Overview
This project converts plain English prompts into accurate, executable SQL queries using **Google Gemini Pro**. It enables non-technical stakeholders and analysts to query relational databases (SQLite / MySQL / PostgreSQL) simply by typing natural language questions.

## Features
- Convert natural language to SQL using Gemini Pro LLM.
- Real-time query generation and execution via a Streamlit web UI.
- Support for multiple relational databases (SQLite, MySQL, PostgreSQL).
- Prompt engineering and templates to improve query accuracy and context awareness.
- Secure handling of credentials using environment variables.
- Basic ambiguity detection and user-friendly error messages.

## Tech Stack
- **LLM:** Google Gemini Pro (via Gemini/Google APIs)
- **Frontend / UI:** Streamlit
- **Backend:** Python (requests / google-auth or official client)
- **Databases:** SQLite, MySQL, PostgreSQL
- **Deployment:** Streamlit Cloud (hosted at the live demo URL above)

## Quickstart (Local)
1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\\Scripts\\activate      # Windows
   ```

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables (example):
   ```bash
   export GEMINI_API_KEY="your_gemini_api_key"
   export DATABASE_URL="postgresql://user:password@host:port/dbname"
   ```

   On Windows (PowerShell):
   ```powershell
   $env:GEMINI_API_KEY="your_gemini_api_key"
   $env:DATABASE_URL="postgresql://user:password@host:port/dbname"
   ```

5. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage Examples
- **User prompt:** `Show top 10 customers by total revenue in 2024`
  - **Generated SQL (example):**
    ```sql
    SELECT customer_id, customer_name, SUM(amount) AS total_revenue
    FROM sales
    WHERE sale_date >= '2024-01-01' AND sale_date <= '2024-12-31'
    GROUP BY customer_id, customer_name
    ORDER BY total_revenue DESC
    LIMIT 10;
    ```

- **User prompt:** `Count orders per region for January 2025`
  - **Generated SQL (example):**
    ```sql
    SELECT region, COUNT(*) AS orders_count
    FROM orders
    WHERE order_date >= '2025-01-01' AND order_date <= '2025-01-31'
    GROUP BY region;
    ```

## Prompt Engineering & Best Practices
- Provide schema context or upload small schema snippets for better accuracy.
- Use explicit date formats when asking time-range queries.
- If results seem ambiguous, the app suggests clarifying questions before execution.

## Security Considerations
- Never hard-code API keys or database credentials.
- Use environment variables and a secrets manager in production.
- Limit database permissions for the app user (read-only when possible).
- Sanitize and preview generated SQL before executing on production databases.

## Notes on Model Behavior
- Gemini Pro generates SQL based on the prompt plus any schema/context supplied.
- Always review generated SQL before running against production data.
- Complex analytic queries or application-specific logic may require manual adjustments.

## Contributing
Contributions, bug reports, and feature requests are welcome. Open an issue or PR with a clear description.

## License
This project is distributed under the MIT License. See `LICENSE` for details.
