---
aid: business-software-and-services-reviews-g2
url: https://raw.githubusercontent.com/api-evangelist/business-software-and-services-reviews-g2/refs/heads/main/apis.yml
name: Business Software and Services Reviews | G2
tags:
  - B2B
  - SaaS
  - Software Reviews
  - Buyer Intent
  - Competitive Intelligence
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-07-11'
modified: '2026-04-23'
position: Consumer
description: G2 is the world's largest and most trusted software marketplace. More than 90 million people annually use G2 to make smarter software decisions based on authentic peer reviews. Find the right software and services based on real user reviews.
apis:
  - aid: business-software-and-services-reviews-g2:g2-api-v2
    name: G2 API V2
    tags:
      - B2B
      - Software Reviews
      - Buyer Intent
      - Competitive Intelligence
    humanURL: https://data.g2.com/api/v2/docs/index.html
    baseURL: https://data.g2.com/api/v2/
    properties:
      - url: https://data.g2.com/api/v2/docs/index.html
        type: Documentation
      - url: https://documentation.g2.com/
        type: Portal
    description: The G2 API V2 provides programmatic access to G2's software reviews, buyer intent signals, competitive intelligence, and product data. Uses OAuth 2.0 for authentication. Enables integration of G2 buyer intent data into CRM, marketing automation, and sales workflows.
    features:
      - OAuth 2.0 Authentication
      - Buyer Intent Signals
      - Competitive Intelligence Data
      - Review Analytics
      - Company Research Activity Tracking
      - Software Product Data
    useCases:
      - CRM integration for buyer intent signals
      - Competitive research and tracking
      - Sales prospecting with intent data
      - Marketing campaign targeting
      - Software evaluation workflows
  - aid: business-software-and-services-reviews-g2:g2-buyer-intent-data
    name: G2 Buyer Intent Data API
    tags:
      - B2B
      - Buyer Intent
      - SaaS
    humanURL: https://documentation.g2.com/docs/buyer-intent-data-reference
    baseURL: https://data.g2.com/api/v2/
    properties:
      - url: https://documentation.g2.com/docs/buyer-intent-data-reference
        type: Documentation
    description: G2 Buyer Intent Data provides signals about companies actively researching software categories, products, and competitors on G2. Tracks nine signal types including profile views, pricing page visits, alternative comparisons, and competitive research. Returns company identification, size, industry, and buying stage data.
    features:
      - Nine Signal Types (Profile, Pricing, Alternatives, Category, Compare, Sponsored Content, Licensed Content, Reference Page, Competitive)
      - Company Identification (Name, Domain, ID)
      - Company Classification (Sector, Industry, Sub-industry)
      - Organization Size Data
      - Buying Stage Classification (Awareness, Consideration, Decision)
      - Activity Level Metrics (Low, Medium, High)
      - Page-Level Visit Data
    useCases:
      - Identify in-market buyers researching your product
      - Prioritize sales outreach by buying stage
      - Monitor competitive research activity
      - Personalize marketing based on buyer intent
      - Account-based marketing (ABM) targeting
  - aid: business-software-and-services-reviews-g2:g2-mcp-server
    name: G2 MCP Server
    tags:
      - B2B
      - AI Integration
      - MCP
      - Buyer Intent
    humanURL: https://documentation.g2.com/docs/g2-mcp-server
    properties:
      - url: https://documentation.g2.com/docs/g2-mcp-server
        type: Documentation
    description: The G2 MCP (Model Context Protocol) Server enables AI assistants like Claude to access G2 data. Uses OAuth for authentication via browser sign-in. Provides access to buyer intent intelligence, competitive intelligence, and review analytics within AI workflows.
    features:
      - OAuth Authentication
      - Buyer Intent Intelligence
      - Competitive Intelligence
      - Review Analytics
      - AI Integration Support
    useCases:
      - AI-powered sales intelligence
      - Automated competitive research in AI workflows
      - LLM-powered buyer intent analysis
common:
  - type: Website
    url: https://www.g2.com/
  - type: Portal
    url: https://documentation.g2.com/
  - type: Privacy Policy
    url: https://www.g2.com/static/privacy
  - type: Developer Documentation
    url: https://documentation.g2.com/docs/integrations
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
