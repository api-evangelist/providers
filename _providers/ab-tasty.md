---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Ab Tasty Agentic Access
  operation_count: 4
  slug: ab-tasty-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- description: AB Tastys Remote Control API is a developer and QA tool that lets you programmatically drive the AB Tasty SDK from outside your app or page, so you can precisely control and observe experiments withou
  name: AB Tasty Remote Control API
  slug: ab-tasty-remote-control-api
- description: The AB Tasty Public API provides programmatic access to manage campaigns, monitor and control experiments, manage account users, and integrate AB Tasty with third-party tools. It uses OAuth-style cred
  name: AB Tasty Public API
  slug: ab-tasty-public-api
- description: The Activate API from AB Tasty — 1 operation(s) for activate.
  name: AB Tasty Activate API
  slug: ab-tasty-activate-api
- description: Campaign assignment operations
  name: AB Tasty Campaigns API
  slug: ab-tasty-campaigns-api
- description: The Environments API from AB Tasty — 3 operation(s) for environments.
  name: AB Tasty Environments API
  slug: ab-tasty-environments-api
artifact_total: 89
collections:
- collection_type: postman
  name: AB Tasty Decision Activate API
  slug: postman-ab-tasty-activate-api
- collection_type: postman
  name: AB Tasty Decision Activate Campaigns API
  slug: postman-ab-tasty-campaigns-api
- collection_type: postman
  name: AB Tasty Decision Activate Environments API
  slug: postman-ab-tasty-environments-api
- collection_type: postman
  name: AB Tasty Decision Activate Flags API
  slug: postman-ab-tasty-flags-api
- collection_type: postman
  name: AB Tasty Decision Activate Post API
  slug: postman-ab-tasty-post-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AB Tasty Decision Activate API
  slug: open-ab-tasty-activate-api
- collection_type: open
  name: AB Tasty Decision Activate Campaigns API
  slug: open-ab-tasty-campaigns-api
- collection_type: open
  name: AB Tasty Decision Activate Environments API
  slug: open-ab-tasty-environments-api
- collection_type: open
  name: AB Tasty Decision Activate Flags API
  slug: open-ab-tasty-flags-api
- collection_type: open
  name: AB Tasty Decision Activate Post API
  slug: open-ab-tasty-post-api
- collection_type: open
  name: AB Tasty Decision API
  slug: open-decision-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ab-tasty/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ab-tasty-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ab-tasty-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ab-tasty-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ab-tasty
- group: company
  title: ''
  type: Website
  url: https://www.abtasty.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.abtasty.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.abtasty.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.abtasty.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://support.abtasty.com/hc/en-us
- group: commercial
  title: ''
  type: Legal
  url: https://www.abtasty.com/legal-notices/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abtasty.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flagship-io
- group: build
  title: ''
  type: CLI
  url: https://github.com/flagship-io/abtasty-cli
- group: build
  title: MCP Server
  type: Tools
  url: https://github.com/flagship-io/mcp-server
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/rules/ab-tasty-spectral-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://www.abtasty.com/feed/
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/vocabulary/ab-tasty-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-ld/ab-tasty-decision-api-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.abtasty.com/llms.txt
created: '2025-06-05'
description: At AB Tasty, we are your partner for pushing great ideas even further through optimization. We achieve this by empowering brands to build better experiences using personalization, experimentation, recommendations, merchandising, and the market's only emotions-based segmentation solution.
examples:
- key_count: 5
  name: Decision Api Activation Request Example
  slug: decision-api-activation-request-example
- key_count: 4
  name: Decision Api Batch Activation Item Example
  slug: decision-api-batch-activation-item-example
- key_count: 2
  name: Decision Api Batch Activation Request Example
  slug: decision-api-batch-activation-request-example
- key_count: 3
  name: Decision Api Campaign Example
  slug: decision-api-campaign-example
- key_count: 6
  name: Decision Api Campaign Request Example
  slug: decision-api-campaign-request-example
- key_count: 4
  name: Decision Api Campaign Response Full Example
  slug: decision-api-campaign-response-full-example
- key_count: 2
  name: Decision Api Campaign Response Normal Example
  slug: decision-api-campaign-response-normal-example
- key_count: 2
  name: Decision Api Campaign Response Simple Example
  slug: decision-api-campaign-response-simple-example
- key_count: 2
  name: Decision Api Campaign Variation Example
  slug: decision-api-campaign-variation-example
- key_count: 1
  name: Decision Api Flag Example
  slug: decision-api-flag-example
- key_count: 9
  name: Decision Api Flag Metadata Example
  slug: decision-api-flag-metadata-example
- key_count: 0
  name: Decision Api Flags Response Example
  slug: decision-api-flags-response-example
- key_count: 0
  name: Decision Api Single Campaign Request Example
  slug: decision-api-single-campaign-request-example
features:
- description: Advanced A/B testing with conversion safety mechanisms and unlimited variations
  name: A/B Testing
- description: Server-side feature flags with targeting and gradual rollouts
  name: Feature Flags
- description: Experience customization based on emotional needs and engagement segmentation
  name: Personalization
- description: Unified search, recommendations, and product visibility control
  name: E-Merchandising
- description: Progressive feature release with automatic KPI-triggered rollbacks
  name: Progressive Rollouts
- description: AI-powered prompt-based visual modifications for experiments
  name: AI Visual Editor
- description: Real-time predictive AI for anonymous visitor personalization targeting 90% of visitors
  name: AdaptiveCX
- description: Test multiple variables simultaneously across web and mobile
  name: Multivariate Testing
finops:
- name: Ab Tasty Finops
  service_category: Experimentation / Personalization
  slug: ab-tasty-finops
image: /assets/icons/ab-tasty.png
integrations:
- description: Partnership with Google Cloud for infrastructure and analytics integration
  name: Google Cloud
- description: Connect with analytics platforms via the integration hub for data sharing
  name: Analytics Tools
- description: Customer Data Platform integrations for enhanced visitor profiling
  name: CDPs
- description: OpenFeature provider integration for standardized feature flag management
  name: OpenFeature
- description: Edge function integration with Vercel for server-side experimentation
  name: Vercel
- description: Cloudflare Worker integration for edge-based feature experimentation
  name: Cloudflare
- description: AWS Lambda integration for serverless feature experimentation
  name: AWS Lambda
- description: Fastly worker integration for CDN-level feature experimentation
  name: Fastly
- description: Akamai worker integration for CDN-level feature experimentation
  name: Akamai
- description: Shopify Hydrogen framework integration for headless commerce experimentation
  name: Shopify Hydrogen
json_schemas:
- name: ActivationRequest
  property_count: 5
  slug: decision-api-activation-request
- name: BatchActivationItem
  property_count: 4
  slug: decision-api-batch-activation-item
- name: BatchActivationRequest
  property_count: 2
  slug: decision-api-batch-activation-request
- name: CampaignRequest
  property_count: 6
  slug: decision-api-campaign-request
- name: CampaignResponseFull
  property_count: 4
  slug: decision-api-campaign-response-full
- name: CampaignResponseNormal
  property_count: 2
  slug: decision-api-campaign-response-normal
- name: CampaignResponseSimple
  property_count: 2
  slug: decision-api-campaign-response-simple
- name: Campaign
  property_count: 3
  slug: decision-api-campaign
- name: CampaignVariation
  property_count: 2
  slug: decision-api-campaign-variation
- name: FlagMetadata
  property_count: 9
  slug: decision-api-flag-metadata
- name: Flag
  property_count: 2
  slug: decision-api-flag
- name: FlagsResponse
  property_count: 0
  slug: decision-api-flags-response
- name: SingleCampaignRequest
  property_count: 0
  slug: decision-api-single-campaign-request
json_structures:
- name: Decision Api Activation Request Structure
  property_count: 5
  slug: decision-api-activation-request-structure
- name: Decision Api Batch Activation Item Structure
  property_count: 4
  slug: decision-api-batch-activation-item-structure
- name: Decision Api Batch Activation Request Structure
  property_count: 2
  slug: decision-api-batch-activation-request-structure
- name: Decision Api Campaign Request Structure
  property_count: 6
  slug: decision-api-campaign-request-structure
- name: Decision Api Campaign Response Full Structure
  property_count: 4
  slug: decision-api-campaign-response-full-structure
- name: Decision Api Campaign Response Normal Structure
  property_count: 2
  slug: decision-api-campaign-response-normal-structure
- name: Decision Api Campaign Response Simple Structure
  property_count: 2
  slug: decision-api-campaign-response-simple-structure
- name: Decision Api Campaign Structure
  property_count: 3
  slug: decision-api-campaign-structure
- name: Decision Api Campaign Variation Structure
  property_count: 2
  slug: decision-api-campaign-variation-structure
- name: Decision Api Flag Metadata Structure
  property_count: 9
  slug: decision-api-flag-metadata-structure
- name: Decision Api Flag Structure
  property_count: 2
  slug: decision-api-flag-structure
- name: Decision Api Flags Response Structure
  property_count: 0
  slug: decision-api-flags-response-structure
- name: Decision Api Single Campaign Request Structure
  property_count: 0
  slug: decision-api-single-campaign-request-structure
jsonld:
- class_count: 13
  name: Ab Tasty Decision Api Context
  property_count: 29
  slug: ab-tasty-decision-api-context
layout: provider
modified: '2026-05-19'
name: AB Tasty
nav: Providers
network: true
overview: 'AB Tasty publishes 3 APIs on the [APIs.io](https://apis.io/) network: Activate API, Campaigns API, and Environments API. Tagged areas include Aggregation, Experimentation, Feature Flags, Personalization, and A/B Testing.


  The AB Tasty catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AB Tasty''s developer surface includes authentication, developer portal, documentation, pricing, support, legal docs, CLI, and 13 more developer resources.'
plans:
- name: Ab Tasty Plans Pricing
  plan_count: 4
  slug: ab-tasty-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Ab Tasty Rate Limits
  slug: ab-tasty-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: AB Tasty API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ab-tasty-jsonschema-spectral-rules
- effective_rule_count: 87
  extends:
  - spectral:oas
  name: AB Tasty API Rules
  rule_count: 46
  severity_counts:
    error: 13
    hint: 0
    info: 6
    warn: 27
  slug: ab-tasty-spectral-rules
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 44.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 78.2
    developer_ergonomics: 66.7
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/screenshots/ab-tasty-2026-06-20T163043.png
security:
- kind: authentication
  name: Ab Tasty Authentication
  slug: ab-tasty-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ab Tasty Domain Security
  slug: ab-tasty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ab-tasty
tags:
- Aggregation
- Experimentation
- Feature Flags
- Personalization
- A/B Testing
use_cases:
- description: Run A/B tests and multivariate experiments on websites to optimize conversion rates
  name: Web Experimentation
- description: Multi-channel feature testing across devices via API or SDK implementation
  name: Feature Experimentation
- description: Backend and edge worker experiments using the Decision API
  name: Server-Side Testing
- description: Merchandising, recommendations, and personalized product experiences
  name: E-commerce Optimization
- description: Gradual feature rollouts with automated rollback based on KPI monitoring
  name: Progressive Deployment
- description: AI-driven real-time personalization for anonymous visitors
  name: Anonymous Personalization
website: https://www.abtasty.com/
---
