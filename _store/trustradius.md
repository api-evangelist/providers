---
aid: trustradius
url: https://raw.githubusercontent.com/api-evangelist/trustradius/refs/heads/main/apis.yml
name: TrustRadius
description: TrustRadius is a B2B buyer intelligence and software review platform that helps technology buyers make confident purchasing decisions and enables vendors to turn verified customer reviews into demand generation. Founded in 2012 and headquartered in Austin, Texas, TrustRadius hosts in-depth verified reviews averaging 400+ words, and provides vendors with downstream intent data showing who is actively researching their products, competitors, and categories. The platform offers REST APIs for accessing product review data, buyer intent signals, and content licensing capabilities, with integrations into Salesforce, HubSpot, 6sense, Demandbase, LinkedIn, Marketo, and Snowflake. Authentication uses API key access from the TrustRadius Vendor Portal.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - B2B Software Reviews
  - Buyer Intelligence
  - Intent Data
  - Software Reviews
  - Reviews
  - Product Reviews
  - Categories
access: 3rd-Party
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: trustradius:trustradius-public-api
    name: TrustRadius Public API
    tags:
      - B2B Software Reviews
      - Product Reviews
      - Reviews
      - Software Categories
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trustradius.com/v1
    humanURL: https://apidocs.trustradius.com/
    properties:
      - url: https://apidocs.trustradius.com/
        type: Documentation
      - url: https://apidocs.trustradius.com/docs/public-api/ZG9jOjQ1Mg-trust-radius-api
        type: Documentation
      - url: https://trustradius.freshdesk.com/support/solutions/articles/43000639047
        type: Authentication
      - url: https://raw.githubusercontent.com/api-evangelist/trustradius/refs/heads/main/openapi/trustradius-public-openapi.yml
        type: OpenAPI
    description: The TrustRadius Public API provides programmatic access to product data, verified user reviews, TrustRadius scores (trScores), software categories, and aggregate rating information. Vendors can retrieve their product profile, reviews written by customers, category information, and competitive comparison data. Authentication uses an API key obtained from the TrustRadius Vendor Portal Integrations section. The API is a REST-based service returning JSON responses.
  - aid: trustradius:trustradius-intent-data-api
    name: TrustRadius Downstream Intent Data API
    tags:
      - Intent Data
      - Buyer Intelligence
      - B2B
      - ABM
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trustradius.com/v1
    humanURL: https://solutions.trustradius.com/intent-data/
    properties:
      - url: https://solutions.trustradius.com/intent-data/
        type: Documentation
      - url: https://solutions.trustradius.com/integrations/
        type: Documentation
      - url: https://apidocs.trustradius.com/
        type: Documentation
    description: The TrustRadius Downstream Intent Data API delivers buyer and deal intelligence, revealing which accounts are actively researching a vendor's products, competitor products, and software categories on TrustRadius. The API provides account-level intent signals that can be integrated with Salesforce, HubSpot, 6sense, Demandbase, Marketo, LinkedIn Matched Audiences, and Snowflake for account-based marketing and sales acceleration workflows.
  - aid: trustradius:trustradius-reviews-api
    name: TrustRadius Reviews API
    tags:
      - Reviews
      - B2B Software Reviews
      - Product Reviews
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trustradius.com/v1
    humanURL: https://apidocs.trustradius.com/
    properties:
      - url: https://apidocs.trustradius.com/
        type: Documentation
      - url: https://trustradius.freshdesk.com/support/solutions/articles/43000639047
        type: Authentication
      - url: https://raw.githubusercontent.com/api-evangelist/trustradius/refs/heads/main/openapi/trustradius-reviews-openapi.yml
        type: OpenAPI
    description: The TrustRadius Reviews API provides access to verified user reviews for software products, including detailed review content (400+ words), ratings across multiple dimensions (usability, support, likelihood to recommend), reviewer information, and pros/cons data. Vendors can retrieve reviews for their own products and export review content for content licensing and syndication programs.
  - aid: trustradius:trustradius-content-syndication-api
    name: TrustRadius Content Syndication API
    tags:
      - Content Licensing
      - Reviews
      - Marketing
      - B2B
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trustradius.com/v1
    humanURL: https://solutions.trustradius.com/products/
    properties:
      - url: https://solutions.trustradius.com/products/
        type: Documentation
      - url: https://apidocs.trustradius.com/
        type: Documentation
    description: The TrustRadius Content Syndication API (TrustQuotes) enables vendors to extract and embed customer review quotes across marketing channels. Businesses can retrieve licensed review excerpts, quotes, and ratings for use in digital advertising, landing pages, email campaigns, and sales collateral. Supports the Integrated Content Syndication Network for broad review distribution.
common:
  - url: https://www.trustradius.com/
    name: TrustRadius Website
    type: Website
  - url: https://solutions.trustradius.com/
    name: TrustRadius for Vendors
    type: Portal
  - url: https://apidocs.trustradius.com/
    name: API Documentation
    type: Documentation
  - url: https://trustradius.freshdesk.com/support/solutions/articles/43000639047
    name: API Key Access
    type: Authentication
  - url: https://solutions.trustradius.com/integrations/
    name: Integrations
    type: Integrations
  - url: https://solutions.trustradius.com/products/
    name: Products
    type: Products
  - url: https://www.trustradius.com/legal/terms-of-use
    name: Terms of Use
    type: TermsOfService
  - url: https://www.trustradius.com/legal/privacy-policy
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://www.linkedin.com/company/trustradius
    name: TrustRadius on LinkedIn
    type: LinkedIn
  - url: https://twitter.com/TrustRadius
    name: TrustRadius on X (Twitter)
    type: X
  - url: https://github.com/trustradius
    name: TrustRadius on GitHub
    type: GitHub
  - url: https://raw.githubusercontent.com/api-evangelist/trustradius/refs/heads/main/rules/trustradius-rules.yml
    name: Spectral Rules
    type: SpectralRules
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
