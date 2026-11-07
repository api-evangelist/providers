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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bespoke Labs Agentic Access
  operation_count: 1
  slug: bespoke-labs-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.bespokelabs.ai
  baseurl_source: declared
  description: The Nimble API from Bespoke Labs — 1 operation(s) for nimble.
  name: Bespoke Labs Nimble API
  slug: bespoke-labs-nimble-api
- baseURL: https://api.bespokelabs.ai
  baseurl_source: declared
  description: The Viewer API from Bespoke Labs — 4 operation(s) for viewer.
  name: Bespoke Labs Viewer API
  slug: bespoke-labs-viewer-api
artifact_total: 8
collections:
- collection_type: open
  name: Argus Minicheck API
  slug: open-bespoke-labs-minicheck-api
common:
- group: other
  href: https://artifacts.apis.io/bespoke-labs/overlays/bespoke-labs-minicheck-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bespoke-labs-minicheck-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/bespoke-labs/agentic-access/bespoke-labs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bespoke-labs-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bespoke-labs/authentication/bespoke-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bespoke-labs-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bespoke-labs/security/bespoke-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bespoke-labs-domain-security.yml
- group: build
  href: https://artifacts.apis.io/bespoke-labs/packages/bespoke-labs-packages.yml
  title: ''
  type: Packages
  url: packages/bespoke-labs-packages.yml
- group: build
  href: https://artifacts.apis.io/bespoke-labs/packages/bespoke-labs-packages.yml
  title: ''
  type: SDKs
  url: packages/bespoke-labs-packages.yml
- group: agent
  href: https://artifacts.apis.io/bespoke-labs/well-known/bespoke-labs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bespoke-labs-well-known.yml
- group: agent
  href: https://artifacts.apis.io/bespoke-labs/mcp/bespoke-labs-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bespoke-labs-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bespoke-labs/llms/bespoke-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bespoke-labs-llms.txt
- group: design
  href: https://artifacts.apis.io/bespoke-labs/conformance/bespoke-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bespoke-labs-conformance.yml
- group: design
  href: https://artifacts.apis.io/bespoke-labs/errors/bespoke-labs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bespoke-labs-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bespoke-labs/lifecycle/bespoke-labs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bespoke-labs-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bespoke-labs/conventions/bespoke-labs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bespoke-labs-conventions.yml
- group: design
  href: https://artifacts.apis.io/bespoke-labs/data-model/bespoke-labs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bespoke-labs-data-model.yml
- group: agent
  href: https://artifacts.apis.io/bespoke-labs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bespokelabs.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bespokelabs.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bespokelabs.ai/models/bespoke-minicheck/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bespokelabs.ai/bespoke-curator/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://console.bespokelabs.ai
- group: operate
  title: ''
  type: Support
  url: https://bespokelabs.ai/contact
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/KqpXvpzVBS
- group: company
  title: ''
  type: Blog
  url: https://bespokelabs.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bespokelabsai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bespokelabs.ai/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bespokelabs.ai/legal/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://bespokelabs.ai
created: '2026-07-17'
description: Bespoke Labs is an applied AI research lab building environment infrastructure, data curation, and evaluation tooling for AI agents and post-training. Its open-source Bespoke Curator library generates high-quality synthetic data at scale for model finetuning and structured extraction, and its Bespoke MiniCheck ("Argus") API offers a lightweight grounded-factuality / hallucination-detection service that scores whether a claim is supported by a given context. The lab is also known for OpenThoughts reasoning datasets, Terminal-Bench, the GEPA prompt optimizer, MiniChart, and OpenThinker. Backed by 8VC, Mayfield, and Wing Venture Capital.
image: https://framerusercontent.com/images/3uXQTaKpkGh6gD7qAWsAwPMhk.png
layout: provider
modified: '2026-07-18'
name: Bespoke Labs
nav: Providers
network: true
overview: 'Bespoke Labs publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Nimble API and Viewer API. Tagged areas include Company, Artificial Intelligence, Machine Learning, LLM, and Synthetic Data.


  The Bespoke Labs catalog on APIs.io includes 1 Spectral governance ruleset.


  Bespoke Labs'' developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 20 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Bespoke Labs API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: bespoke-labs-rules
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 43.6
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 50.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bespoke-labs/bespoke-labs-2026-07-25T202750.png
security:
- kind: authentication
  name: Bespoke Labs Authentication
  slug: bespoke-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bespoke Labs Domain Security
  slug: bespoke-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Fact-check a claim with Bespoke MiniCheck
  slug: bespoke-labs-factcheck
slug: bespoke-labs
tags:
- Company
- Artificial Intelligence
- Machine Learning
- LLM
- Synthetic Data
- Data Curation
- Fact Checking
- Hallucination Detection
- AI Agents
- Evaluation
website: https://bespokelabs.ai
---
