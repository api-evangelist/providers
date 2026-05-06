---
aid: bloomberg-query-language-bql
name: Bloomberg Query Language (BQL)
description: Bloomberg Query Language (BQL) is a proprietary query language for accessing, filtering, aggregating, and computing on Bloomberg's financial data universe. BQL enables users to write flexible data requests that go beyond standard API fields, supporting derived calculations, time series expressions, and complex filtering of securities and data points. Available in the Bloomberg Terminal, Excel Add-in, and via API.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-query-language-bql/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - BQL
  - Query Language
  - Financial Data
  - Analytics
  - Data Query
  - Bloomberg
apis:
  - aid: bloomberg-query-language-bql:bql-api
    name: Bloomberg Query Language (BQL) API
    description: Execute BQL queries programmatically via the Bloomberg API to retrieve custom computed financial data, filtered security sets, and time series expressions from Bloomberg's data universe. Accessible via BLPAPI and Bloomberg Excel Add-in.
    humanURL: https://www.bloomberg.com/professional/support/api-library/
    baseURL: blpapi://localhost:8194
    tags:
      - BQL
      - Query API
      - Financial Data
      - Time Series
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
  - aid: bloomberg-query-language-bql:bql-excel
    name: BQL in Bloomberg Excel Add-in
    description: Use Bloomberg Query Language directly in Microsoft Excel to execute complex data queries and retrieve computed results in spreadsheet cells. Supports multi-row outputs, time series, and calculated fields.
    humanURL: https://www.bloomberg.com/professional/solution/bloomberg-excel/
    baseURL: https://bloomberg.com/bql-excel
    tags:
      - BQL
      - Excel
      - Spreadsheet
      - Formulas
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/bloomberg-excel/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: Features
    data:
      - name: Security Universe Filtering
        description: Filter securities using complex logical and conditional expressions.
      - name: Derived Calculations
        description: Compute derived financial metrics and ratios in BQL expressions.
      - name: Time Series Expressions
        description: Build time series queries for historical data analysis.
      - name: Aggregation Functions
        description: Aggregate data with sum, average, rank, and other functions.
      - name: Cross-Asset Data Access
        description: Query Bloomberg data across equities, fixed income, FX, and commodities.
      - name: BQL in Excel
        description: Execute BQL queries directly in Excel cells for spreadsheet analysis.
  - type: UseCases
    data:
      - name: Quantitative Screening
        description: Screen securities using complex fundamental and technical criteria.
      - name: Custom Analytics
        description: Create custom financial metrics not available as standard data fields.
      - name: Portfolio Analysis
        description: Analyze portfolio characteristics using flexible BQL expressions.
      - name: Backtesting
        description: Access historical data via BQL time series for strategy backtesting.
      - name: Risk Reporting
        description: Compute and aggregate risk metrics across portfolios using BQL.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
