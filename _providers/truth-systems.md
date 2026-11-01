---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: The Get Context Output API from Truth Systems — 1 operation(s) for get context output.
  name: Truth Systems Get Context Output API
  slug: truth-systems-get-context-output-api
artifact_total: 6
collections:
- collection_type: open
  name: Gateway Get Context Output API
  slug: open-truth-systems-get-context-output-api
common:
- group: other
  href: https://artifacts.apis.io/truth-systems/capabilities/truth-systems-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/truth-systems-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/truth-systems/overlays/truth-systems-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/truth-systems-gateway-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/truth-systems/security/truth-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/truth-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.truthsystems.ai
- group: start
  title: ''
  type: Portal
  url: https://docs.truthsystems.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.truthsystems.ai/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TruthSystems
- group: operate
  title: ''
  type: Support
  url: mailto:info@truthsystems.com
- group: agent
  href: https://artifacts.apis.io/truth-systems/llms/truth-systems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/truth-systems-llms.txt
- group: agent
  href: https://artifacts.apis.io/truth-systems/mcp/truth-systems-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/truth-systems-mcp.yml
- group: build
  href: https://artifacts.apis.io/truth-systems/packages/truth-systems-packages.yml
  title: ''
  type: Packages
  url: packages/truth-systems-packages.yml
- group: build
  href: https://artifacts.apis.io/truth-systems/packages/truth-systems-packages.yml
  title: ''
  type: SDKs
  url: packages/truth-systems-packages.yml
- group: auth
  href: https://artifacts.apis.io/truth-systems/authentication/truth-systems-authentication.yml
  title: ''
  type: Authentication
  url: authentication/truth-systems-authentication.yml
- group: design
  href: https://artifacts.apis.io/truth-systems/conventions/truth-systems-conventions.yml
  title: ''
  type: Conventions
  url: conventions/truth-systems-conventions.yml
- group: design
  href: https://artifacts.apis.io/truth-systems/errors/truth-systems-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/truth-systems-problem-types.yml
- group: design
  href: https://artifacts.apis.io/truth-systems/conformance/truth-systems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/truth-systems-conformance.yml
- group: design
  href: https://artifacts.apis.io/truth-systems/data-model/truth-systems-data-model.yml
  title: ''
  type: DataModel
  url: data-model/truth-systems-data-model.yml
- group: agent
  href: https://artifacts.apis.io/truth-systems/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Truth Systems builds AI governance and hallucination-detection infrastructure for regulated industries, with a focus on legal firms. Gateway, its core API product, fact-checks LLM-generated text against customer source documents in real time - decomposing a claim into statements, retrieving evidence, and returning SUPPORTS / REFUTES / NOT_ENOUGH_INFO verdicts with character-level evidence spans. Gateway deploys into the customer's own AWS or Azure account via Terraform, with a Python SDK. The company also offers Charter (AI governance for human users) and Alexandria (agent-focused governance), and is backed by Lightspeed Venture Partners.
image: https://www.truthsystems.ai/truthsystems-logo.svg
layout: provider
mcp_servers:
- description: 'Truth Systems operates a hosted, remote MCP server on its documentation site (Mintlify-hosted, streamable HTTP). The server is read-only and scoped to the Truth Systems Docs content: it exposes docume'
  name: Truth Systems Docs
  slug: truth-systems-docs
modified: '2026-07-21'
name: Truth Systems
nav: Providers
network: true
overview: 'Truth Systems publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Get Context Output API. Tagged areas include Company, Artificial Intelligence, AI Governance, Hallucination Detection, and Fact Checking.


  Truth Systems'' developer surface includes developer portal, documentation, support, authentication, and 14 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 44.4
    developer_ergonomics: 63.7
    discoverability: 56.7
    operational_transparency: 5.3
  previous_composite: 30.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/truth-systems/truth-systems-2026-09-02T164426.png
security:
- kind: authentication
  name: Truth Systems Authentication
  slug: truth-systems-authentication
  summary_line: aws-iam/apiKey · 2 schemes
- kind: domain-security
  name: Truth Systems Domain Security
  slug: truth-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Fact-check a claim against source documents with Gateway
  slug: truth-systems-fact-check-claim
slug: truth-systems
tags:
- Company
- Artificial Intelligence
- AI Governance
- Hallucination Detection
- Fact Checking
- Compliance
- Legal
website: https://www.truthsystems.ai
---
