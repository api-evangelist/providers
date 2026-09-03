---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: semantha's standardized RESTful web service for semantic processing of text documents and structured data extraction. Resources are organized under /api (info, domains/{domain}/referencedocuments, set
  name: semantha REST API
  slug: semantha-rest-api
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/aleph-alpha/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thingsthinking-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.semantha.de/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.semantha.de/experten/
- group: docs
  title: ''
  type: Documentation
  url: https://pypi.org/project/semantha-sdk/
- group: company
  title: ''
  type: Blog
  url: https://www.semantha.de/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.semantha.de/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.semantha.de/contact/
- group: start
  title: ''
  type: SignUp
  url: https://www.semantha.de/request/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.semantha.de/privacy-notice-and-terms-of-use/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.semantha.de/terms-conditions/
- group: build
  title: ''
  type: Packages
  url: packages/thingsthinking-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/thingsthinking-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thingsthinking-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thingsthinking-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thingsthinking-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.semantha.de/data-security/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thingsthinking-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/thingsthinking-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thingsthinking-llms.txt
created: '2026-07-17'
description: Thingsthinking GmbH is a Karlsruhe, Germany-based semantic AI company and the maker of semantha, an adaptive AI platform for text-driven business processes. semantha applies semantic natural-language understanding to documents and unstructured text for use cases such as contract and document analysis, semantic comparison, enterprise search, requirements and specifications analysis, classification and clustering, ESG report analysis, compliance management, correspondence automation, and risk analysis in underwriting. The platform is delivered as a comprehensive REST API with a first-party Python SDK (semantha-sdk), authenticated via OAuth2 client credentials / OpenID Connect (with a legacy per-domain API key), hosted exclusively in the EU and operated in a GDPR/DSGVO-compliant manner. Thingsthinking was surfaced as a portfolio company of Earlybird and has since been acquired by Aleph Alpha.
image: https://www.semantha.de/wp-content/uploads/cropped-semantha_favicon_wordpress.png
layout: provider
modified: '2026-07-21'
name: Thingsthinking
nav: Providers
network: true
overview: 'Thingsthinking publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semantic AI, Natural Language Processing, Document Analysis, and Enterprise Search.


  Thingsthinking''s developer surface includes documentation, engineering blog, support, signup flow, authentication, changelog, and 14 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 29.3
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thingsthinking/refs/heads/main/screenshots/thingsthinking-2026-09-02T163526.png
security:
- kind: authentication
  name: Thingsthinking Authentication
  slug: thingsthinking-authentication
  summary_line: oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Thingsthinking Domain Security
  slug: thingsthinking-domain-security
  summary_line: TLSv1.2 · DMARC
slug: thingsthinking
tags:
- Company
- Semantic AI
- Natural Language Processing
- Document Analysis
- Enterprise Search
- Contract Analysis
- Text Analytics
- Machine-Learning
- Compliance
- REST API
- Germany
website: https://www.semantha.de/
---
