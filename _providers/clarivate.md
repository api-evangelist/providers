---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Clarivate Agentic Access
  operation_count: 4
  slug: clarivate-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Web of Science APIs deliver publication and citation data drawn from the curated Web of Science Core Collection, supporting bibliometric analysis, research evaluation, and institutional assessment wor
  name: Web of Science APIs
  slug: web-of-science-api
- description: The Derwent Innovation API provides programmatic access to Derwent World Patents Index data, including normalized patent records, families, and citations used for IP intelligence and competitive analy
  name: Derwent Innovation API
  slug: derwent-innovation-api
- description: Cortellis APIs expose the Clarivate life sciences intelligence platform, covering drug pipelines, clinical trials, regulatory intelligence, deals, and competitive intelligence for biopharma and medica
  name: Cortellis APIs
  slug: cortellis-api
- description: The InCites API provides programmatic access to the Clarivate research benchmarking platform, enabling institutional research performance analytics built on Web of Science data.
  name: InCites Benchmarking and Analytics API
  slug: incites-api
- description: The Documents API from Clarivate — 2 operation(s) for documents.
  name: Clarivate Documents API
  slug: clarivate-documents-api
- description: The Journals API from Clarivate — 2 operation(s) for journals.
  name: Clarivate Journals API
  slug: clarivate-journals-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clarivate Web of Science Starter Documents API
  slug: open-clarivate-documents-api
- collection_type: open
  name: Clarivate Web of Science Starter Documents Journals API
  slug: open-clarivate-journals-api
- collection_type: open
  name: Clarivate Web of Science Starter API
  slug: open-clarivate
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clarivate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clarivate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clarivate-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clarivate
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clarivate
- group: company
  title: ''
  type: Website
  url: https://clarivate.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.clarivate.com/
- group: other
  title: ''
  type: API Catalog
  url: https://developer.clarivate.com/apis
- group: operate
  title: ''
  type: Support
  url: https://support.clarivate.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clarivate.com/privacy-center/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clarivate.com/legal-center/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clarivate-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/clarivate-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://clarivate.com/news/
created: '2024-12-16'
description: 'Clarivate is a global information services company providing data, insights, and analytics across academia, government, life sciences, healthcare, and intellectual property. Clarivate exposes a unified developer portal at developer.clarivate.com that catalogs APIs across its product families: Web of Science for publication and citation data, Derwent for patent data, Cortellis for life sciences and drug pipeline intelligence, and supporting tools such as InCites and ScholarOne. APIs are subscription-based and authenticated with per-API keys issued through the developer portal after subscription approval.'
finops:
- name: Clarivate Finops
  service_category: API
  slug: clarivate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clarivate.png
jsonld:
- class_count: 14
  name: Clarivate Context
  property_count: 0
  slug: clarivate-context
layout: provider
modified: '2026-04-23'
name: Clarivate
nav: Providers
network: true
overview: 'Clarivate publishes 2 APIs on the [APIs.io](https://apis.io/) network: Documents API and Journals API. Tagged areas include Analytics, Citations, Data, Drug Pipeline, and Insights.


  The Clarivate catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clarivate''s developer surface includes authentication, developer portal, support, engineering blog, and 10 more developer resources.'
plans:
- name: Clarivate Plans Pricing
  plan_count: 3
  slug: clarivate-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Clarivate Rate Limits
  slug: clarivate-rate-limits
rules:
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Clarivate API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: clarivate-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 45.5
    contract_quality: 55.8
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 45.5
    operational_transparency: 10.5
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clarivate/refs/heads/main/screenshots/clarivate-2026-06-20T174437.png
security:
- kind: authentication
  name: Clarivate Authentication
  slug: clarivate-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Clarivate Domain Security
  slug: clarivate-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clarivate
tags:
- Analytics
- Citations
- Data
- Drug Pipeline
- Insights
- Intellectual Property
- Life Sciences
- Patents
- Publications
- Research
website: https://clarivate.com/
---
