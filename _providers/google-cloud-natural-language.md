---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Natural Language Agentic Access
  operation_count: 5
  slug: google-cloud-natural-language-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 1
apis:
- baseURL: https://language.googleapis.com
  baseurl_source: declared
  description: The documents:analyzeEntities API from Google Cloud Natural Language — 1 operation(s) for documents:analyzeentities.
  name: Google Cloud Natural Language documents:analyzeEntities API
  slug: google-cloud-natural-language-documents-analyzeentities-api
- baseURL: https://language.googleapis.com
  baseurl_source: declared
  description: The documents:analyzeSentiment API from Google Cloud Natural Language — 1 operation(s) for documents:analyzesentiment.
  name: Google Cloud Natural Language documents:analyzeSentiment API
  slug: google-cloud-natural-language-documents-analyzesentiment-api
- baseURL: https://language.googleapis.com
  baseurl_source: declared
  description: The documents:analyzeSyntax API from Google Cloud Natural Language — 1 operation(s) for documents:analyzesyntax.
  name: Google Cloud Natural Language documents:analyzeSyntax API
  slug: google-cloud-natural-language-documents-analyzesyntax-api
- baseURL: https://language.googleapis.com
  baseurl_source: declared
  description: The documents:annotateText API from Google Cloud Natural Language — 1 operation(s) for documents:annotatetext.
  name: Google Cloud Natural Language documents:annotateText API
  slug: google-cloud-natural-language-documents-annotatetext-api
- baseURL: https://language.googleapis.com
  baseurl_source: declared
  description: The documents:classifyText API from Google Cloud Natural Language — 1 operation(s) for documents:classifytext.
  name: Google Cloud Natural Language documents:classifyText API
  slug: google-cloud-natural-language-documents-classifytext-api
artifact_total: 26
collections:
- collection_type: postman
  name: Google Cloud Natural Language documents:analyzeEntities API
  slug: postman-google-cloud-natural-language-documents-analyzeentities-api
- collection_type: postman
  name: Google Cloud Natural Language documents:analyzeEntities documents:analyzeSentiment API
  slug: postman-google-cloud-natural-language-documents-analyzesentiment-api
- collection_type: postman
  name: Google Cloud Natural Language documents:analyzeEntities documents:analyzeSyntax API
  slug: postman-google-cloud-natural-language-documents-analyzesyntax-api
- collection_type: postman
  name: Google Cloud Natural Language documents:analyzeEntities documents:annotateText API
  slug: postman-google-cloud-natural-language-documents-annotatetext-api
- collection_type: postman
  name: Google Cloud Natural Language documents:analyzeEntities documents:classifyText API
  slug: postman-google-cloud-natural-language-documents-classifytext-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Natural Language documents:analyzeEntities API
  slug: open-google-cloud-natural-language-documents-analyzeentities-api
- collection_type: open
  name: Google Cloud Natural Language documents:analyzeEntities documents:analyzeSentiment API
  slug: open-google-cloud-natural-language-documents-analyzesentiment-api
- collection_type: open
  name: Google Cloud Natural Language documents:analyzeEntities documents:analyzeSyntax API
  slug: open-google-cloud-natural-language-documents-analyzesyntax-api
- collection_type: open
  name: Google Cloud Natural Language documents:analyzeEntities documents:annotateText API
  slug: open-google-cloud-natural-language-documents-annotatetext-api
- collection_type: open
  name: Google Cloud Natural Language documents:analyzeEntities documents:classifyText API
  slug: open-google-cloud-natural-language-documents-classifytext-api
- collection_type: open
  name: Google Cloud Natural Language API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-natural-language/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-natural-language-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-natural-language-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-natural-language-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/natural-language
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/natural-language/docs/quickstarts
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/natural-language/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/natural-language/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/natural-language/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/natural-language/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
created: '2026-03-13'
description: Google Cloud Natural Language API provides natural language understanding technologies including sentiment analysis, entity recognition, entity sentiment analysis, content classification, and syntax analysis. It helps developers extract insights from unstructured text.
finops:
- name: Google Cloud Natural Language Finops
  service_category: API
  slug: google-cloud-natural-language-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-natural-language.png
json_schemas:
- name: Document Analysis
  property_count: 3
  slug: document-analysis
jsonld:
- class_count: 14
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Cloud Natural Language
nav: Providers
network: true
overview: 'Google Cloud Natural Language publishes 5 APIs on the [APIs.io](https://apis.io/) network, including documents:analyzeEntities API, documents:analyzeSentiment API, documents:analyzeSyntax API, and 2 more. Tagged areas include Entity Recognition, Google Cloud, Machine-Learning, Natural Language Processing, and Sentiment Analysis.


  The Google Cloud Natural Language catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Natural Language''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, and 9 more developer resources.'
plans:
- name: Google Cloud Natural Language Plans Pricing
  plan_count: 3
  slug: google-cloud-natural-language-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Google Cloud Natural Language Rate Limits
  slug: google-cloud-natural-language-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Natural Language API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-natural-language-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 12
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 60.0
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-natural-language/refs/heads/main/screenshots/google-cloud-natural-language-2026-06-20T182126.png
security:
- kind: domain-security
  name: Google Cloud Natural Language Domain Security
  slug: google-cloud-natural-language-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Natural Language Vulnerability Disclosure
  slug: google-cloud-natural-language-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-natural-language
tags:
- Entity Recognition
- Google Cloud
- Machine-Learning
- Natural Language Processing
- Sentiment Analysis
- Text Analysis
website: https://cloud.google.com/natural-language
---
