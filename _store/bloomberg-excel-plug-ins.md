---
aid: bloomberg-excel-plug-ins
name: Bloomberg Excel Plug-ins
description: Bloomberg Excel Plug-ins integrate Bloomberg market data, analytics, and functions directly into Microsoft Excel. The Bloomberg Add-in for Excel provides the BDH, BDP, BDS, and other Bloomberg formula functions to pull real-time and historical data, enabling quantitative analysis, financial modeling, and reporting without leaving the spreadsheet environment.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-excel-plug-ins/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Excel
  - Spreadsheet
  - Financial Modeling
  - Market Data
  - Bloomberg
  - Add-in
apis:
  - aid: bloomberg-excel-plug-ins:bloomberg-excel-addin
    name: Bloomberg Excel Add-in
    description: The Bloomberg Add-in for Microsoft Excel provides formula functions including BDP (Bloomberg Data Point), BDH (Bloomberg Data History), BDS (Bloomberg Data Set), and BQL for accessing Bloomberg data directly in spreadsheets.
    humanURL: https://www.bloomberg.com/professional/support/software-updates/
    baseURL: https://bloomberg.com/excel
    tags:
      - Excel
      - Add-in
      - BDP
      - BDH
      - BDS
      - Formulas
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/software-updates/
  - aid: bloomberg-excel-plug-ins:bloomberg-bql-excel
    name: Bloomberg BQL in Excel
    description: Access Bloomberg Query Language (BQL) directly within Excel to run flexible, custom queries for financial data, analytics, and derived metrics using the Bloomberg BQL Add-in.
    humanURL: https://www.bloomberg.com/professional/solution/bloomberg-excel/
    baseURL: https://bloomberg.com/bql-excel
    tags:
      - BQL
      - Excel
      - Query Language
      - Analytics
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/bloomberg-excel/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://developer.bloomberg.com/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: Features
    data:
      - name: BDP Formula
        description: Bloomberg Data Point formula for real-time and static data retrieval in Excel.
      - name: BDH Formula
        description: Bloomberg Data History formula for historical time series data retrieval.
      - name: BDS Formula
        description: Bloomberg Data Set formula for multi-cell data retrieval and tables.
      - name: BQL Integration
        description: Bloomberg Query Language support directly in Excel for advanced custom queries.
      - name: Real-Time Updates
        description: Automatic data refresh for real-time market data in Excel cells.
      - name: Portfolio Analysis Templates
        description: Pre-built Excel templates for portfolio analysis, risk, and reporting.
  - type: UseCases
    data:
      - name: Financial Modeling
        description: Build discounted cash flow models and valuation models with live Bloomberg data.
      - name: Portfolio Reporting
        description: Create automated portfolio reports with real-time and historical data.
      - name: Risk Analysis
        description: Pull pricing, volatility, and correlation data for risk calculations.
      - name: Market Research
        description: Analyze market trends and securities data without leaving Excel.
      - name: Quantitative Analysis
        description: Run quantitative screens and backtests using Bloomberg historical data in Excel.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
