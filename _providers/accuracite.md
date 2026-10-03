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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.4
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Accuracite Agentic Access
  operation_count: 2
  slug: accuracite-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: 'Synchronous REST API for citation verification and claim-to-source lookup. Two operations, both POST and both keyed by an X-API-Key header: /api/v1/verify checks a citation string (or a bare URL, or a'
  name: AccuraCite API
  slug: accuracite-api
- baseURL: https://accuracite.com/api/v1
  baseurl_source: declared
  description: The Generate API from AccuraCite — 1 operation(s) for generate.
  name: AccuraCite Generate API
  slug: accuracite-generate-api
- baseURL: https://accuracite.com/api/v1
  baseurl_source: declared
  description: The Verify API from AccuraCite — 1 operation(s) for verify.
  name: AccuraCite Verify API
  slug: accuracite-verify-api
artifact_total: 18
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/json-ld/accuracite-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/accuracite-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/vocabulary/accuracite-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/accuracite-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/mcp/accuracite-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/accuracite-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/packages/accuracite-packages.yml
  title: ''
  type: SDKs
  url: packages/accuracite-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/packages/accuracite-packages.yml
  title: ''
  type: Packages
  url: packages/accuracite-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/agentic-access/accuracite-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/accuracite-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/rules/accuracite-rules.yml
  title: ''
  type: Spectral
  url: rules/accuracite-rules.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/security/accuracite-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/accuracite-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/hosts/accuracite-hosts.yml
  title: ''
  type: Hosts
  url: hosts/accuracite-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/vendors/accuracite-vendors.yml
  title: ''
  type: Vendors
  url: vendors/accuracite-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AccuraCite
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/security/accuracite-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/accuracite-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://accuracite.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/security/accuracite-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accuracite-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/llms/accuracite-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accuracite-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/authentication/accuracite-authentication.yml
  title: ''
  type: Authentication
  url: authentication/accuracite-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/rate-limits/accuracite-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/accuracite-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/plans/accuracite-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/accuracite-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/errors/accuracite-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/accuracite-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/conventions/accuracite-conventions.yml
  title: ''
  type: Conventions
  url: conventions/accuracite-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/data-model/accuracite-data-model.yml
  title: ''
  type: DataModel
  url: data-model/accuracite-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/conformance/accuracite-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accuracite-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/lifecycle/accuracite-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/accuracite-lifecycle.yml
- group: docs
  title: ''
  type: Documentation
  url: https://accuracite.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://accuracite.com/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://accuracite.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://accuracite.com/blog
- group: operate
  title: ''
  type: Support
  url: https://accuracite.com/feedback
- group: start
  title: ''
  type: SignUp
  url: https://accuracite.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accuracite.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accuracite.com/privacy
- group: other
  title: ''
  type: ApiCatalog
  url: https://accuracite.com/.well-known/api-catalog
- group: auth
  title: ''
  type: SecurityTxt
  url: https://accuracite.com/.well-known/security.txt
created: '2026-08-31'
description: 'AccuraCite verifies bibliographies and finds real citations, catching AI-hallucinated references before they are published. Every citation supplied as raw text, BibTeX, RIS or an uploaded PDF is checked against eight academic indexes -- OpenAlex, Crossref, Semantic Scholar, PubMed, DBLP, arXiv, CORE and Google Scholar -- and returned as verified, mismatch or not_found, with the matched bibliographic record and a field-level list of what disagreed. A second surface runs the other direction: given a claim, it returns real papers whose abstracts actually support it rather than papers whose titles merely look related. Both are exposed over a small synchronous REST API (POST /api/v1/verify and POST /api/v1/generate) keyed by an X-API-Key header and metered from a shared monthly credit pool. AccuraCite is a solo-founder product built by a computer-science PhD after finding fabricated citations in a co-authored, partly AI-drafted paper.'
image: https://accuracite.com/static/img/og-image.png
json_schemas:
- name: GenerateRequest
  property_count: 2
  slug: accuracite-generate-request
- name: VerifyBatchRequest
  property_count: 1
  slug: accuracite-verify-batch-request
- name: VerifyCitationFieldsRequest
  property_count: 1
  slug: accuracite-verify-citation-fields-request
- name: VerifyCitationsBatchRequest
  property_count: 1
  slug: accuracite-verify-citations-batch-request
- name: VerifyResult
  property_count: 6
  slug: accuracite-verify-result
- name: VerifySingleRequest
  property_count: 1
  slug: accuracite-verify-single-request
jsonld:
- class_count: 11
  name: Accuracite Context
  property_count: 32
  slug: accuracite-context
layout: provider
mcp_servers:
- description: ''
  name: AccuraCite MCP Server
  slug: accuracite-mcp-server
modified: '2026-08-31'
name: AccuraCite
nav: Providers
network: true
overview: 'AccuraCite publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Generate API, Verify API, and 1 more. Tagged areas include Citations, Research, Bibliography, Academic, and Verification.


  The AccuraCite catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AccuraCite''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, signup flow, and 27 more developer resources.'
plans:
- name: Accuracite Plans Pricing
  plan_count: 5
  slug: accuracite-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Accuracite Rate Limits
  slug: accuracite-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: AccuraCite API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: accuracite-rules
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 24.1
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 68.4
    developer_ergonomics: 44.6
    discoverability: 81.7
    operational_transparency: 36.8
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 30.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/accuracite/refs/heads/main/screenshots/accuracite-2026-09-02T144112.png
security:
- kind: authentication
  name: Accuracite Authentication
  slug: accuracite-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Accuracite Domain Security
  slug: accuracite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Accuracite Vulnerability Disclosure
  slug: accuracite-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: accuracite
tags:
- Citations
- Research
- Bibliography
- Academic
- Verification
- AI Safety
website: https://accuracite.com/
---
