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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 6.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: OAuth 2.0 REST API for requesting a consenting user's genetic trait reports from Genomelink. A report is fetched by trait name and population (for example GET /v1/reports/eye-color/?population=europea
  name: Genomelink Developer API
  slug: genomelink-developer-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://genomelink.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://genomelink.io/developers/
- group: start
  title: ''
  type: SignUp
  url: https://genomelink.io/signup/
- group: start
  title: ''
  type: Login
  url: https://genomelink.io/login/
- group: operate
  title: ''
  type: Support
  url: https://genomelink.io/help
- group: company
  title: ''
  type: Blog
  url: https://genomelink.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://genomelink.io/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.genomelink.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/genomelink
- group: build
  title: ''
  type: Packages
  url: packages/awakens-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/awakens-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/awakens-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/awakens-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/awakens-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/awakens-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/awakens-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/awakens-domain-security.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/awakens-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/awakens-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/awakens-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/awakens-oauth-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/awakens-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/awakens-data-model.yml
created: '2026-07-17'
description: AWAKENS (operating the consumer product Genomelink at genomelink.io) is a personal-genomics company that lets people upload the raw DNA data they exported from AncestryDNA, 23andMe, or MyHeritage and receive additional ancestry, trait, nutrition, and wellness reports interpreted from a knowledge base of 100,000+ SNPs across 50+ genetic traits. For developers, AWAKENS published the Genomelink Developer API — an OAuth 2.0 (authorization-code) REST API that lets third-party apps request a user's genetic trait reports (for example eye-color by population) after the user consents, plus an enterprise reports endpoint. Official Python (`genomelink`) and Node.js (`genomelink-node`) SDKs were shipped on PyPI and npm. The public developer API is currently marked "not available" on the developers page, so the artifacts here capture the documented OAuth surface, SDKs, and test credentials from AWAKENS' own first-party sources.
image: https://genomelink.io/favicon.ico
layout: provider
modified: '2026-07-18'
name: AWAKENS
nav: Providers
network: true
overview: 'AWAKENS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Genomics, DNA, Bioinformatics, and Health.


  AWAKENS''s developer surface includes signup flow, support, engineering blog, authentication, sandbox, and 19 more developer resources.'
random_paper: 11
scopes:
- name: Awakens Scopes
  scope_count: 0
  slug: awakens-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 29.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/awakens/refs/heads/main/screenshots/awakens-2026-07-25T202019.png
security:
- kind: authentication
  name: Awakens Authentication
  slug: awakens-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Awakens Domain Security
  slug: awakens-domain-security
  summary_line: TLSv1.3 · DMARC
slug: awakens
tags:
- Company
- Genomics
- DNA
- Bioinformatics
- Health
- Consumer Genetics
- Ancestry
- Authentication
- Personal Genomics
website: https://genomelink.io
---
