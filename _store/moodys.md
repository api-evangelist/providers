---
aid: moodys
url: https://github.com/api-search/moodys/apis.yml
apis:
  - aid: moodys:moodys
    name: Moody's KYC API
    tags:
      - Anti-Money Laundering
      - Compliance
      - Entity Verification
      - KYC
      - Risk
      - Screening
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.kompany.com/kycapi/discover
    properties:
      - url: https://www.kompany.com/kycapi/console-v2
        type: Documentation
      - url: |-

          https://www.kompany.com/kycapi/docs/resources/resources/customer-facing-documents/generate-a-client-from-openapi-definition
        type: OpenAPI
    description: "With evolving regulatory pressures and bad actors becoming increasingly adept at concealing themselves, the need for deep understanding of business partners, customers, and other third parties is more critical than ever to mitigate reputational damage and risk exposure. Moody\x19 s KYC technology, data, and analytical capabilities provide industry-leading customer solutions for Know Your Customer, anti-money laundering, compliance, and counter-party risk."
  - aid: moodys:data-buffet-api
    name: Moody's Data Buffet API
    tags:
      - Demographics
      - Economic Data
      - Forecasts
      - Time Series
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.economy.com
    contact:
      - FN: API Evangelist
        email: kin@apievangelist.com
    humanURL: https://www.economy.com/products/tools/data-buffet
    properties:
      - url: https://api.economy.com/data/v1/swagger
        type: Documentation
      - url: https://github.com/moodysanalytics/databuffet-api-codesamples
        type: GitHubOrganization
      - url: openapi/moodys-data-buffet-api-openapi.yml
        type: OpenAPI
      - url: json-schema/moodys-time-series-schema.json
        type: JSONSchema
      - url: json-ld/moodys-context.jsonld
        type: JSONLD
    description: Moody's Analytics Data Buffet application program interface enables you to retrieve economic, demographic and financial time series directly from the Data Buffet repository, including international and subnational economic and demographic time series data and forecasts.
  - aid: moodys:scenario-studio-api
    name: Moody's Scenario Studio API
    tags:
      - Economic Models
      - Forecasting
      - Macroeconomic
      - Scenarios
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.economy.com
    contact:
      - FN: API Evangelist
        email: kin@apievangelist.com
    humanURL: https://hub.moodysanalytics.com/products
    properties:
      - url: https://api.economy.com/scenario-studio/v2/swagger
        type: Documentation
      - url: https://github.com/moodysanalytics/scenario-studio-api-codesamples
        type: GitHubOrganization
    description: Scenario Studio delivers Moody's Analytics Global Macroeconomic Model that emphasizes stability, forecast accuracy and consistency. The API retrieves custom scenarios generated in the Scenario Studio platform.
  - aid: moodys:autocycle-api
    name: Moody's AutoCycle API
    tags:
      - Automotive
      - Forecasts
      - Residual Value
      - Vehicle Pricing
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.economy.com
    contact:
      - FN: API Evangelist
        email: kin@apievangelist.com
    humanURL: https://hub.moodysanalytics.com/products
    properties:
      - url: https://api.economy.com/autocycle/v1/swagger
        type: Documentation
    description: Retrieves forecasts of vehicle prices from AutoCycle models. AutoCycle is a software solution to forecast car prices, incorporating economic data and scenarios from Moody's Analytics.
  - aid: moodys:eccl-api
    name: Moody's Consumer Credit Loss Forecasts API
    tags:
      - Consumer Credit
      - Credit Loss
      - Forecasts
      - Risk
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.economy.com
    contact:
      - FN: API Evangelist
        email: kin@apievangelist.com
    humanURL: https://hub.moodysanalytics.com/products
    properties:
      - url: https://api.economy.com/eccl/v1/swagger
        type: Documentation
    description: Retrieves expected consumer credit loss forecasts under baseline and stress scenarios. The ECCL API combines customer data, economic data from Moody's Analytics, and consumer credit data for credit risk modeling.
  - aid: moodys:municipal-api
    name: Moody's Municipal Probability of Default API
    tags:
      - Credit Risk
      - Forecasts
      - Municipal
      - Probability of Default
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.economy.com
    contact:
      - FN: API Evangelist
        email: kin@apievangelist.com
    humanURL: https://hub.moodysanalytics.com/products
    properties:
      - url: https://api.economy.com/muni/v1/swagger
        type: Documentation
    description: Retrieves probability of default and loss rates for the municipal market under baseline and stress scenarios. Enables scoring of municipal credit risk using Moody's Analytics models.
  - aid: moodys:edf-x-api
    name: Moody's EDF-X API
    tags:
      - Credit Risk
      - Expected Default Frequency
      - Probability of Default
      - Risk Assessment
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://hub.moodysanalytics.com
    contact:
      - FN: API Evangelist
        email: kin@apievangelist.com
    humanURL: https://hub.moodysanalytics.com/products
    properties:
      - url: https://hub.moodysanalytics.com/products
        type: Documentation
    description: The EDF-X API provides easy access to probability of default calculations for approximately 400 million companies globally via the Orbis database. It provides a PD term structure with annualized, cumulative, and forward PD values, implied ratings, and confidence indicators.
  - aid: moodys:newsedge-api
    name: Moody's NewsEdge API
    tags:
      - Media
      - News
      - Real-Time Data
      - Social Media
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://hub.moodysanalytics.com
    contact:
      - FN: API Evangelist
        email: kin@apievangelist.com
    humanURL: https://hub.moodysanalytics.com/products
    properties:
      - url: https://hub.moodysanalytics.com/products
        type: Documentation
    description: Bring together real-time news sources, and the best of the business web and social media to empower decision makers. The NewsEdge API provides access to Moody's 24,000+ news sources for integration into custom applications.
  - aid: moodys:quiqspread-api
    name: Moody's QUIQSpread API
    tags:
      - Automation
      - Banking
      - Financial Spreading
      - Financial Statements
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://hub.moodysanalytics.com
    contact:
      - FN: API Evangelist
        email: kin@apievangelist.com
    humanURL: https://hub.moodysanalytics.com/products
    properties:
      - url: https://hub.moodysanalytics.com/products
        type: Documentation
    description: Moody's Analytics QUIQspread is an intelligent, financial spreading software that will accelerate a company's spreading process. The API enables integration of automated financial statement processing into banking workflows.
  - aid: moodys:capital-risk-analyzer-api
    name: Moody's Capital Risk Analyzer API
    tags:
      - Banking
      - Capital Planning
      - Risk
      - Stress Testing
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://hub.moodysanalytics.com
    contact:
      - FN: API Evangelist
        email: kin@apievangelist.com
    humanURL: https://hub.moodysanalytics.com/products
    properties:
      - url: https://hub.moodysanalytics.com/products
        type: Documentation
    description: Moody's Analytics Capital Risk Analyzer solution is a tool that projects key capital ratios and credit metrics based on various strategic and economic scenarios for capital planning and stress testing such as DFAST and EBA.
  - aid: moodys:climate-on-demand-api
    name: Moody's Climate on Demand API
    tags:
      - Climate Risk
      - Environmental
      - Insurance
      - Physical Risk
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://developer.rms.com
    contact:
      - FN: API Evangelist
        email: kin@apievangelist.com
    humanURL: https://developer.rms.com/climate-on-demand
    properties:
      - url: https://developer.rms.com/climate-on-demand
        type: Documentation
    description: The Climate On Demand API enables financial services organizations to build physical climate risk applications that leverage the power of the Intelligent Risk Platform.
  - aid: moodys:location-intelligence-api
    name: Moody's Location Intelligence API
    tags:
      - Geospatial
      - Insurance
      - Location
      - Risk Data
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://developer.rms.com
    contact:
      - FN: API Evangelist
        email: kin@apievangelist.com
    humanURL: https://hub.moodysanalytics.com/products
    properties:
      - url: https://hub.moodysanalytics.com/products
        type: Documentation
    description: Location Intelligence API delivers more than 100 data layers across multiple kinds of data including hazard, location, risk score, model, and exposure data to help improve business decisions and better manage risk.
  - aid: moodys:risk-modeler-api
    name: Moody's Risk Modeler API
    tags:
      - Catastrophe Modeling
      - Insurance
      - Risk
      - Underwriting
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://developer.rms.com
    contact:
      - FN: API Evangelist
        email: kin@apievangelist.com
    humanURL: https://developer.rms.com/risk-modeler
    properties:
      - url: https://developer.rms.com/risk-modeler
        type: Documentation
    description: The Risk Modeler API enables you to manage end-to-end catastrophe modeling workflows using Moody's RMS models for portfolios, accounts, and locations on the Intelligent Risk Platform.
  - aid: moodys:intelligent-risk-platform-api
    name: Moody's Intelligent Risk Platform API
    tags:
      - Insurance
      - Platform
      - Reinsurance
      - Risk Management
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://developer.rms.com
    contact:
      - FN: API Evangelist
        email: kin@apievangelist.com
    humanURL: https://developer.rms.com/platform/docs/introduction
    properties:
      - url: https://developer.rms.com/platform/docs/introduction
        type: Documentation
    description: Moody's RMS Platform APIs are a collection of REST APIs that enable Intelligent Risk Platform tenants to work more efficiently. Risk Modeler, UnderwriteIQ, TreatyIQ, and ExposureIQ tenants can use them to manage bulk data transfers, automate catastrophe modeling workflows, and generate reports.
  - aid: moodys:commercial-real-estate-api
    name: Moody's Commercial Real Estate API
    tags:
      - Commercial Real Estate
      - CRE
      - Location Score
      - Property
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://hub.moodysanalytics.com
    contact:
      - FN: API Evangelist
        email: kin@apievangelist.com
    humanURL: https://hub.moodysanalytics.com/products
    properties:
      - url: https://hub.moodysanalytics.com/products
        type: Documentation
    description: API solutions to empower commercial real estate developers to build systems and platforms faster. Brings efficiency and automation into your organization, including the Commercial Location Score API and MA CRE API.
name: Moody's
tags:
  - Climate Risk
  - Compliance
  - Credit Risk
  - Economic Data
  - Entity Verification
  - Financial Analytics
  - Insurance
  - KYC
  - Risk
  - Screening
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.kompany.com/
    type: Portal
  - url: https://www.kompany.com/kycapi/dashboard/plans
    type: Plans
  - url: https://www.kompany.com/kycapi/docs/quick-start
    type: GettingStarted
  - url: https://www.kompany.com/kycapi/console
    type: Console
  - url: https://www.kompany.com/kycapi/community/developer-news
    type: Blog
  - url: https://www.kompany.com/kycapi/docs/guides/guides/get-started
    type: GettingStarted
  - url: https://www.kompany.com/kycapi/docs/guides/guides/get-started/sandbox-overview
    type: Sandbox
  - url: https://www.kompany.com/kycapi/docs/guides/guides/use-cases
    type: UseCases
  - url: https://www.kompany.com/kycapi/docs/resources
    type: Resources
  - type: Features
    data:
      - 'Moody''s: API access via partner / B2B contracts only'
      - No public API pricing published — contact enterprise sales
      - Moody's Analytics APIs (Ratings, Risk, Economics) are enterprise data subscriptions priced per data product.
    sources:
      - https://developer.moodys.com/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Credit Risk Assessment
        description: Evaluate counterparty credit risk using EDF-X probability of default and loss given default models.
      - name: Regulatory Stress Testing
        description: Generate stress scenarios for DFAST, CCAR, and EBA regulatory compliance testing.
      - name: Commercial Lending
        description: Automate financial spreading and credit analysis workflows for commercial loan underwriting.
      - name: Catastrophe Modeling
        description: Model insurance portfolio risk exposure using catastrophe models and location intelligence.
  - type: Integrations
    data:
      - name: Orbis Database
        description: Integration with the Orbis database covering 400 million companies for credit risk analysis.
      - name: Intelligent Risk Platform
        description: Platform integration for catastrophe modeling, underwriting, and reinsurance workflows.
      - name: News Sources
        description: Integration with 24,000+ news sources for real-time media monitoring and sentiment analysis.
  - url: https://www.kompany.com/kycapi/connections
    type: Integrations
  - url: https://kycapi-status.kompany.com/
    type: StatusPage
  - url: https://hub.moodysanalytics.com/
    type: Portal
  - url: https://hub.moodysanalytics.com/products
    type: Documentation
  - url: https://hub.moodysanalytics.com/gettingstarted
    type: GettingStarted
  - url: https://hub.moodysanalytics.com/contact
    type: Contact
  - url: https://developer.rms.com/
    type: Portal
  - url: https://www.economy.com/products/tools/api
    type: Documentation
  - url: https://github.com/moodysanalytics
    type: GitHubOrganization
  - url: https://www.rms.com/developer-resources
    type: Resources
created: '2024-09-25T00:00:00.000Z'
modified: '2026-05-04'
position: Consuming
description: Moody's provides a comprehensive suite of APIs spanning KYC compliance, economic data and forecasting, credit risk analytics, insurance and catastrophe modeling, climate risk, commercial real estate, and news aggregation. With evolving regulatory pressures and increasingly complex risk landscapes, Moody's technology, data, and analytical capabilities power industry-leading solutions across financial services, insurance, and risk management.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
