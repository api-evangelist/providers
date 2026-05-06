---
aid: crunchbase
url: https://raw.githubusercontent.com/api-evangelist/crunchbase/refs/heads/main/apis.yml
x-type: company
name: Crunchbase
description: Crunchbase is a business data platform tracking companies, investors, funding rounds, acquisitions, and IPOs across the global startup and private market ecosystem. Its REST API (v4) provides programmatic access to over 600 endpoints powering customer-facing products, workflow enrichment, and AI training data.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Business Data
  - Funding
  - Investments
  - Startups
  - Private Markets
  - Firmographics
type: Index
access: 3rd-Party
specificationVersion: '0.19'
created: '2026-03-24'
modified: '2026-04-28'
apis:
  - aid: crunchbase:crunchbase-api
    name: Crunchbase API
    description: The Crunchbase v4 REST API provides programmatic access to Crunchbase's business data covering organizations, people, investors, funding rounds, acquisitions, and IPOs. Supports entity lookups, structured search, autocomplete, and deleted entity feeds. Authentication is by API key (X-cb-user-key header).
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.crunchbase.com/api/v4
    humanURL: https://data.crunchbase.com/docs
    tags:
      - Business Data
      - Funding
      - Investments
      - Startups
      - REST
    properties:
      - url: https://data.crunchbase.com/docs
        type: Documentation
      - url: https://data.crunchbase.com/docs/authentication
        type: Authentication
      - url: https://data.crunchbase.com/docs/rate-limiting
        type: RateLimits
      - url: https://data.crunchbase.com/docs/changelog
        type: ChangeLog
      - url: openapi/crunchbase-openapi.yml
        type: OpenAPI
      - url: json-schema/crunchbase-organization-schema.json
        type: JSONSchema
      - url: json-ld/crunchbase-context.jsonld
        type: JSONLDContext
features:
  - name: Entity Lookups
    description: Retrieve organizations, people, funding rounds, acquisitions, and IPOs by UUID or permalink.
  - name: Structured Search
    description: POST-based search with field, operator, and value clauses across all entity types.
  - name: Autocomplete
    description: Type-ahead lookups for entities by name across collections.
  - name: Deleted Entity Feeds
    description: Track removed entities for incremental data synchronization.
  - name: Field Selection
    description: Request specific fields and related cards (founders, investments, headquarters) per entity.
  - name: 600+ Endpoints
    description: Round-by-round funding data, firmographics, and predictive intelligence covering private markets.
  - name: API Key Authentication
    description: Header-based API key auth using X-cb-user-key.
  - name: Rate Limited
    description: Per-key rate limits documented at data.crunchbase.com/docs/rate-limiting.
useCases:
  - name: Market Intelligence
    description: Analysts track competitor funding, growth, and acquisition activity.
  - name: Investor Research
    description: VCs and PE firms research portfolio companies, comparable rounds, and lead investors.
  - name: Sales Intelligence and ABM
    description: Sales teams enrich CRM records with firmographics, funding, and headcount data.
  - name: Startup Discovery
    description: Accelerators and corp-dev teams search for organizations matching specific criteria.
  - name: AI Model Training
    description: Foundation model and analytics teams use Crunchbase data to train and evaluate models.
  - name: Customer-Facing Products
    description: SaaS products embed Crunchbase data into dashboards, lead lists, and signals.
common:
  - url: https://www.crunchbase.com/
    name: Crunchbase Website
    type: Website
  - url: https://data.crunchbase.com/docs
    name: API Documentation
    type: Documentation
  - url: https://www.crunchbase.com/register
    name: Sign Up
    type: SignUp
  - url: https://www.crunchbase.com/login
    name: Login
    type: Login
  - url: https://www.crunchbase.com/pricing
    name: Pricing
    type: Pricing
  - url: https://data.crunchbase.com/docs/authentication
    name: Authentication
    type: Authentication
  - url: https://data.crunchbase.com/docs/rate-limiting
    name: Rate Limiting
    type: RateLimits
  - url: https://data.crunchbase.com/docs/changelog
    name: Changelog
    type: ChangeLog
  - url: https://support.crunchbase.com/
    name: Support
    type: Support
  - url: https://www.crunchbase.com/terms-of-service
    name: Terms of Service
    type: TermsOfService
  - url: https://www.crunchbase.com/privacy-policy
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://www.crunchbase.com/blog
    name: Crunchbase Blog
    type: Blog
  - url: https://twitter.com/crunchbase
    name: Crunchbase on X (Twitter)
    type: X
  - url: https://www.linkedin.com/company/crunchbase
    name: Crunchbase on LinkedIn
    type: LinkedIn
  - url: https://www.facebook.com/crunchbase
    name: Crunchbase on Facebook
    type: Facebook
  - url: https://github.com/crunchbase
    name: Crunchbase on GitHub
    type: GitHub
  - url: openapi/crunchbase-openapi.yml
    type: OpenAPI
  - url: json-schema/crunchbase-organization-schema.json
    type: JSONSchema
  - url: json-ld/crunchbase-context.jsonld
    type: JSONLDContext
  - url: rules/crunchbase-rules.yml
    type: SpectralRules
  - url: vocabulary/crunchbase-vocabulary.yml
    type: Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
