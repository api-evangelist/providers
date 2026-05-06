---
aid: circana
url: https://raw.githubusercontent.com/api-evangelist/circana/refs/heads/main/apis.yml
name: Circana
tags:
  - Analytics
  - Consumer Data
  - Market Research
  - Retail
  - CPG
  - Point Of Sale
  - Consumer Insights
  - Business Intelligence
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-01-01'
modified: '2026-04-18'
position: Consumer
description: Circana (formerly IRI and The NPD Group) is the leading advisor on the complexity of consumer behavior, providing data-driven insights, analytics, and technology solutions that help almost 7,000 brands and retailers understand and predict consumer purchasing patterns across retail, CPG, beauty, foodservice, healthcare, and technology sectors covering $4T+ in global consumer spending across 26 industries.
apis:
  - aid: circana:unify-plus-api
    name: Circana Unify+ API
    tags:
      - Business Intelligence
      - Data Visualization
      - Analytics
      - Reporting
    humanURL: https://www.circana.com/solutions/unify-plus
    description: Unify+ is Circana's business intelligence platform that provides access to data visualization, analytics, and reporting capabilities with conversational AI for automated analysis and insights.
    properties:
      - type: Documentation
        url: https://www.circana.com/solutions/unify-plus
  - aid: circana:liquid-data-api
    name: Circana Liquid Data API
    tags:
      - Data Platform
      - Analytics
      - Cloud
      - Data Integration
    humanURL: https://www.circana.com/company/technology
    description: Liquid Data is Circana's cross-industry technology platform providing advanced analytics, data integration, and AI-powered insights deployable across Azure, AWS, Google Cloud, and Oracle Cloud environments.
    properties:
      - type: Documentation
        url: https://www.circana.com/company/technology
      - type: OpenAPI
        url: openapi/circana-liquid-data.yaml
      - type: JSONSchema
        url: json-schema/liquid-data-pos-record-schema.json
        title: POS Record Schema
      - type: JSONSchema
        url: json-schema/liquid-data-market-share-record-schema.json
        title: Market Share Record Schema
      - type: JSONSchema
        url: json-schema/liquid-data-consumer-purchase-record-schema.json
        title: Consumer Purchase Record Schema
      - type: JSONSchema
        url: json-schema/liquid-data-consumer-segment-schema.json
        title: Consumer Segment Schema
      - type: JSONSchema
        url: json-schema/liquid-data-category-detail-schema.json
        title: Category Detail Schema
      - type: JSONSchema
        url: json-schema/liquid-data-brand-detail-schema.json
        title: Brand Detail Schema
      - type: JSONSchema
        url: json-schema/liquid-data-retailer-summary-schema.json
        title: Retailer Summary Schema
      - type: JSONSchema
        url: json-schema/liquid-data-report-detail-schema.json
        title: Report Detail Schema
      - type: JSONSchema
        url: json-schema/liquid-data-export-detail-schema.json
        title: Export Detail Schema
      - type: JSONLD
        url: json-ld/circana-liquid-data-context.jsonld
  - aid: circana:liquid-data-go-api
    name: Circana Liquid Data Go API
    tags:
      - Market Intelligence
      - CPG
      - Analytics
      - Emerging Brands
    humanURL: https://www.circana.com/solutions/liquid-data-go
    description: Liquid Data Go is a turnkey insights solution delivering affordable, actionable market, retailer, and consumer intelligence for emerging and mid-market CPG and general merchandise brands with 15% more market measurement coverage.
    properties:
      - type: Documentation
        url: https://www.circana.com/solutions/liquid-data-go
  - aid: circana:intelligence-suite-api
    name: Circana Intelligence Suite API
    tags:
      - Data Integration
      - Automation
      - Data Harmonization
      - Cloud
    humanURL: https://www.circana.com/solutions/intelligence-suite
    description: Intelligence Suite helps integrate, harmonize, and automate data workflows with hundreds of pre-built connectors for Azure, Snowflake, AWS, Google BigQuery, and Databricks, enabling real-time automation and insights.
    properties:
      - type: Documentation
        url: https://www.circana.com/solutions/intelligence-suite
  - aid: circana:complete-market-api
    name: Circana Complete Market API
    tags:
      - Point Of Sale
      - Market Measurement
      - Retail Analytics
    humanURL: https://www.circana.com/solutions/complete-market
    description: Complete Market provides robust POS measurement for in-store and online sales with fulfillment type breaks and UPC details across CPG categories.
    properties:
      - type: Documentation
        url: https://www.circana.com/solutions/complete-market
  - aid: circana:complete-consumer-api
    name: Circana Complete Consumer API
    tags:
      - Consumer Panel
      - Shopper Insights
      - Purchase Data
    humanURL: https://www.circana.com/solutions/complete-consumer
    description: Complete Consumer combines verified purchase data, survey insights, and advanced shopper panels to provide a 360-degree view of how, where, and why consumers shop across channels.
    properties:
      - type: Documentation
        url: https://www.circana.com/solutions/complete-consumer
  - aid: circana:complete-beauty-api
    name: Circana Complete Beauty API
    tags:
      - Beauty
      - Market Data
      - Prestige
      - Mass Market
    humanURL: https://www.circana.com/solutions/complete-beauty
    description: Complete Beauty offers a holistic view of the beauty industry combining mass and prestige POS data for manufacturers and retailers to track emerging shifts in consumer preferences and category performance.
    properties:
      - type: Documentation
        url: https://www.circana.com/solutions/complete-beauty
  - aid: circana:complete-food-beverage-api
    name: Circana Complete Food and Beverage API
    tags:
      - Food
      - Beverage
      - Foodservice
      - CPG
    humanURL: https://www.circana.com/solutions/complete-food-and-beverage
    description: Complete Food and Beverage unites retail, CPG, foodservice, and consumption data to deliver a complete understanding of U.S. food and beverage consumption patterns.
    properties:
      - type: Documentation
        url: https://www.circana.com/solutions/complete-food-and-beverage
  - aid: circana:liquid-data-collaborate-api
    name: Circana Liquid Data Collaborate API
    tags:
      - Data Collaboration
      - Retail Analytics
      - AI
    humanURL: https://www.circana.com/solutions/liquid-data-collaborate
    description: Liquid Data Collaborate provides AI-powered retail data analysis capabilities for brands, manufacturers, and retailers enabling collaborative insights and data-driven decision making.
    properties:
      - type: Documentation
        url: https://www.circana.com/solutions/liquid-data-collaborate
  - aid: circana:liquid-data-engage-api
    name: Circana Liquid Data Engage API
    tags:
      - Retail Strategy
      - Customer Analytics
      - Data Precision
    humanURL: https://www.circana.com/solutions/liquid-data-engage
    description: Liquid Data Engage propels retailers into a new era of decision-making with precise, customer-centric data for developing retail strategies.
    properties:
      - type: Documentation
        url: https://www.circana.com/solutions/liquid-data-engage
  - aid: circana:liquid-activation-api
    name: Circana Liquid Activation API
    tags:
      - Audience Activation
      - Marketing
      - Advertising
    humanURL: https://www.circana.com/solutions/liquid-activation
    description: Liquid Activation enables marketers to build and activate purchase-based audiences in minutes using deterministic data, integrating with publishers, media platforms, and marketing technologies.
    properties:
      - type: Documentation
        url: https://www.circana.com/solutions/liquid-activation
  - aid: circana:price-promotion-api
    name: Circana Price and Promotion API
    tags:
      - Pricing
      - Promotion
      - Trade Optimization
      - Forecasting
    humanURL: https://www.circana.com/solutions/price-and-promotion
    description: Price and Promotion solutions combine AI models and granular store-level data to optimize pricing strategies, quantify elasticity, and improve promotional efficiency delivering 5% average sales growth.
    properties:
      - type: Documentation
        url: https://www.circana.com/solutions/price-and-promotion
  - aid: circana:retail-media-api
    name: Circana Retail Media API
    tags:
      - Retail Media
      - Advertising
      - ROAS
      - Media Analytics
    humanURL: https://www.circana.com/solutions/retail-media
    description: Retail Media connects shopper analytics to activation, linking marketing to retail sales for longitudinal insights and improved ROAS with AI-driven media channel performance assessment.
    properties:
      - type: Documentation
        url: https://www.circana.com/solutions/retail-media
  - aid: circana:complete-why-api
    name: Circana Complete Why Analytics API
    tags:
      - AI Analytics
      - Sales Performance
      - Diagnostics
    humanURL: https://www.circana.com/solutions/complete-why
    description: Complete Why delivers fast AI-powered insights so teams know what is working, what is not, and where to act next before opportunities disappear.
    properties:
      - type: Documentation
        url: https://www.circana.com/solutions/complete-why
common:
  - type: Portal
    url: https://www.circana.com
  - type: Documentation
    url: https://www.circana.com/solutions
  - type: Blog
    url: https://www.circana.com/intelligence/press-releases
  - type: Customers
    url: https://www.circana.com/case-studies
  - type: TermsOfService
    url: https://www.circana.com/terms-and-conditions
  - type: PrivacyPolicy
    url: https://www.circana.com/the-circana-group-global-privacy-policy-and-notice
  - type: LinkedIn
    url: https://www.linkedin.com/company/wearecircana
  - type: Contact
    url: https://www.circana.com/contact
  - type: Resources
    url: https://www.circana.com/intelligence
  - type: Partners
    url: https://www.circana.com/company/partners
  - type: Training
    url: https://www.circana.com/industry-experts
  - type: Pricing
    url: https://www.circana.com/solutions
  - type: SpectralRules
    url: rules/circana-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/market-intelligence.yaml
    title: Market Intelligence Workflow
  - type: NaftikoCapability
    url: capabilities/shared/liquid-data.yaml
    title: Liquid Data Shared Definition
  - type: Vocabulary
    url: vocabulary/circana-vocabulary.yaml
  - type: Features
    data:
      - name: Liquid Data Platform
        description: Cross-industry data and advanced analytics platform deployable across Azure, AWS, Google Cloud, and Oracle Cloud environments.
      - name: Liquid AI
        description: Next-generation intelligence platform leveraging generative AI to accelerate decision-making and shift focus from hindsight to foresight.
      - name: Conversational AI
        description: AI embedded into Unify+ allowing teams to automate routine analysis and reduce time to insight.
      - name: Complete Market Measurement
        description: Robust POS measurement for in-store and online sales with fulfillment type breaks and UPC details.
      - name: Consumer Panel Data
        description: 360-degree view of U.S. buyers tracking purchases across channels with POS-aligned panel insights.
      - name: Intelligence Suite Connectors
        description: Hundreds of pre-built connectors for Azure, Snowflake, AWS, Google BigQuery, and Databricks integration.
      - name: Purchase-Based Audiences
        description: Build and activate audiences using deterministic purchase data for precision marketing.
      - name: Price Elasticity Modeling
        description: AI models with granular store-level data to quantify price elasticity and promotional efficiency.
      - name: Cross-Industry Coverage
        description: Coverage of $4T+ in global consumer spending across 26 industries in 23 countries.
      - name: Predictive Market Structure
        description: Industry-only predictive market structure based on actual shopper behavior for new product forecasts within 10% accuracy.
  - type: UseCases
    data:
      - name: Market Share Tracking
        description: Track brand and category performance across retail channels with POS and panel data to understand competitive positioning.
      - name: New Product Innovation
        description: Validate new product concepts with custom simulations and predictive market structure analysis to prioritize winning ideas.
      - name: Pricing Optimization
        description: Optimize pricing strategies using AI-driven elasticity models and store-level data to maximize revenue and margin.
      - name: Promotional Planning
        description: Plan and evaluate trade promotions with quantified ROI metrics and scenario modeling for smarter promotional spending.
      - name: Consumer Segmentation
        description: Segment consumers by behavior, demographics, and purchase patterns to tailor marketing and product strategies.
      - name: Retail Media Measurement
        description: Measure retail media campaign performance linking advertising spend to actual sales outcomes for improved ROAS.
      - name: Assortment Optimization
        description: Optimize product mix by category, store, and geography to improve shelf efficiency and drive sales growth.
      - name: Supply Chain Visibility
        description: Monitor near-real-time cross-retailer inventory and distribution data to spot risks and gaps early.
      - name: Audience Activation
        description: Build purchase-based audience segments and activate them across publishers and media platforms in minutes.
      - name: Foodservice Intelligence
        description: Unite retail, CPG, foodservice, and consumption data for a complete picture of food and beverage market dynamics.
  - type: Integrations
    data:
      - name: Snowflake
        description: Access Circana POS and panel data directly within Snowflake Data Cloud for seamless data sharing and collaboration.
      - name: Microsoft Azure
        description: Deploy Liquid Data platform on Azure for cloud-native data integration and analytics workflows.
      - name: Amazon Web Services
        description: Deploy Liquid Data platform on AWS for scalable cloud analytics and data processing.
      - name: Google BigQuery
        description: Connect Circana data to Google BigQuery for large-scale analytics and machine learning workloads.
      - name: Databricks
        description: Integrate Circana data with Databricks for advanced analytics, data engineering, and AI model training.
      - name: LiveRamp
        description: Collaborate on RampIDs with Circana purchase data in Snowflake for privacy-safe audience targeting.
      - name: Oracle Cloud
        description: Deploy Liquid Data platform on Oracle Cloud for enterprise-grade data processing and analytics.
      - name: Google Cloud Platform
        description: Deploy Liquid Data platform on GCP for cloud-based analytics and data integration.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
