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
  band: agent-ready
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
    error_semantics: verified
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
  score: 30.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 38
  human_in_the_loop: 1
  name: Frankieone Agentic Access
  operation_count: 52
  slug: frankieone-agentic-access
  summary_line: 52 operations · 38 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: Manage audit entries
  name: FrankieOne Audit API
  slug: frankieone-audit-api
- description: Manage hosted URLs for an individual
  name: FrankieOne HostedURL API
  slug: frankieone-hostedurl-api
- description: Get a token and/or upload documents to initiate an IDV process
  name: FrankieOne IDV API
  slug: frankieone-idv-api
- description: Manage documents for individuals
  name: FrankieOne Individual Documents API
  slug: frankieone-individual-documents-api
- description: Manage individual entity records
  name: FrankieOne Individual Entities API
  slug: frankieone-individual-entities-api
- description: Manage individual entity record elements
  name: FrankieOne Individual Entity Elements API
  slug: frankieone-individual-entity-elements-api
- description: Manage individual profiles
  name: FrankieOne Individual Profiles API
  slug: frankieone-individual-profiles-api
- description: Manage results for individuals
  name: FrankieOne Individual Results API
  slug: frankieone-individual-results-api
- description: Manage risks associated with an individual
  name: FrankieOne Individual Risks API
  slug: frankieone-individual-risks-api
- description: The Individual Workflows API from FrankieOne — 5 operation(s) for individual workflows.
  name: FrankieOne Individual Workflows API
  slug: frankieone-individual-workflows-api
- description: The Matchlists API from FrankieOne — 6 operation(s) for matchlists.
  name: FrankieOne Matchlists API
  slug: frankieone-matchlists-api
- description: Turn on/off ongoing monitoring for an individual entity
  name: FrankieOne Monitoring API
  slug: frankieone-monitoring-api
- description: The Search API from FrankieOne — 1 operation(s) for search.
  name: FrankieOne Search API
  slug: frankieone-search-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Core V2 API
  slug: open-core-v2
- collection_type: open
  name: Core V2 Audit API
  slug: open-frankieone-audit-api
- collection_type: open
  name: Core V2 Audit HostedURL API
  slug: open-frankieone-hostedurl-api
- collection_type: open
  name: Core V2 Audit IDV API
  slug: open-frankieone-idv-api
- collection_type: open
  name: Core V2 Audit Individual Documents API
  slug: open-frankieone-individual-documents-api
- collection_type: open
  name: Core V2 Audit Individual Entities API
  slug: open-frankieone-individual-entities-api
- collection_type: open
  name: Core V2 Audit Individual Entity Elements API
  slug: open-frankieone-individual-entity-elements-api
- collection_type: open
  name: Core V2 Audit Individual Profiles API
  slug: open-frankieone-individual-profiles-api
- collection_type: open
  name: Core V2 Audit Individual Results API
  slug: open-frankieone-individual-results-api
- collection_type: open
  name: Core V2 Audit Individual Risks API
  slug: open-frankieone-individual-risks-api
- collection_type: open
  name: Core V2 Audit Individual Workflows API
  slug: open-frankieone-individual-workflows-api
- collection_type: open
  name: Core V2 Audit Matchlists API
  slug: open-frankieone-matchlists-api
- collection_type: open
  name: Core V2 Audit Monitoring API
  slug: open-frankieone-monitoring-api
- collection_type: open
  name: Core V2 Audit Search API
  slug: open-frankieone-search-api
- collection_type: open
  name: KYC V2 API
  slug: open-kyc-v2
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/frankieone-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/frankieone-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/frankieone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/frankieone-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FrankieFinancial
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/frankieone
- group: company
  title: ''
  type: Website
  url: https://www.frankieone.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.frankieone.com/
- group: start
  title: ''
  type: Signup
  url: https://www.frankieone.com/contact-us
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.frankieone.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://frankieone.com/frankieone-blog/rss.xml
created: '2025-02-08'
description: FrankieOne is an identity verification, compliance, and fraud prevention platform connecting applications to hundreds of global data sources through a single API for KYC, KYB, document IDV, ongoing monitoring, and matchlist management.
finops:
- name: Frankieone Finops
  service_category: API
  slug: frankieone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/frankieone.png
layout: provider
modified: '2026-05-19'
name: FrankieOne
nav: Providers
network: true
overview: 'FrankieOne publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Audit API, HostedURL API, IDV API, and 10 more. Tagged areas include Identity Verification, KYC, KYB, AML, and Fraud.


  The FrankieOne catalog on APIs.io includes 2 Spectral governance rulesets.


  FrankieOne''s developer surface includes authentication, documentation, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Frankieone Plans Pricing
  plan_count: 3
  slug: frankieone-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Frankieone Rate Limits
  slug: frankieone-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: FrankieOne API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: frankieone-core-rules
- effective_rule_count: 0
  extends: []
  name: FrankieOne API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: frankieone-kyc-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 12
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 63.1
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/frankieone/refs/heads/main/screenshots/frankieone-2026-06-20T181611.png
security:
- kind: authentication
  name: Frankieone Authentication
  slug: frankieone-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Frankieone Domain Security
  slug: frankieone-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Frankieone Trust Center
  slug: frankieone-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: frankieone
tags:
- Identity Verification
- KYC
- KYB
- AML
- Fraud
- Compliance
website: https://www.frankieone.com/
---
