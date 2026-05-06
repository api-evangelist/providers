---
aid: ais
url: https://raw.githubusercontent.com/api-evangelist/ais/refs/heads/main/apis.yml
name: AIS Group
tags:
  - Analytics
  - Finance
  - Insurance
  - Investment Analytics
  - Risk Management
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
description: AIS Group is an analytics and investment management firm providing independent, data-driven insights across global financial markets. The firm combines macroeconomic research with quantitative analytics to deliver non-correlated investment strategies for financial advisors and institutional clients, with a focus on commodity, currency, equity, and fixed-income market analysis.
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: ais:ais-client-portal
    name: AIS Client Portal
    description: The AIS Client Portal provides investment analytics, portfolio management, and reporting tools for financial advisors and individual investors. The portal enables access to AIS investment strategies, performance data, risk analytics, and account management features through a secure web-based interface.
    humanURL: https://clients.aisgroup.com
    tags:
      - Analytics
      - Client Portal
      - Investment Analytics
      - Portfolio Management
      - Reporting
    properties:
      - type: Documentation
        url: https://www.aisgroup.com
      - type: Login
        url: https://clients.aisgroup.com
common:
  - type: Website
    url: https://www.aisgroup.com
  - type: Contact
    url: https://www.aisgroup.com/contact
  - type: PrivacyPolicy
    url: https://www.aisgroup.com/privacy-policy
  - type: Features
    data:
      - name: Global Investment Analytics
        description: Quantitative analysis across commodity, currency, equity, and fixed-income markets to identify investment opportunities.
      - name: Non-Correlated Strategies
        description: Investment strategies designed to provide diversifying return streams with low correlations to traditional and alternative investments.
      - name: Macroeconomic Research
        description: Independent macroeconomic and intermarket analysis supporting tactical asset allocation and risk management decisions.
      - name: Client Portfolio Reporting
        description: Comprehensive portfolio reporting and performance analytics accessible via the secure client portal.
      - name: Risk Management Analytics
        description: Risk-adjusted return analysis and portfolio risk metrics to support investment decision-making.
  - type: UseCases
    data:
      - name: Portfolio Diversification
        description: Financial advisors use AIS analytics to identify non-correlated investment strategies that reduce portfolio concentration risk.
      - name: Tactical Asset Allocation
        description: Institutional investors leverage AIS macroeconomic research to inform tactical shifts across asset classes.
      - name: Alternative Investment Research
        description: Investment professionals access AIS quantitative models to evaluate alternative and global investment opportunities.
      - name: Performance Benchmarking
        description: Clients use the portal's reporting tools to benchmark portfolio performance against relevant indices and peer groups.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
