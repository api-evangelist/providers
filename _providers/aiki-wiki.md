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
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 48
  human_in_the_loop: 7
  name: Aiki Wiki Agentic Access
  operation_count: 85
  slug: aiki-wiki-agentic-access
  summary_line: 85 operations · 48 acting · 7 human-in-the-loop
api_count: 1
apis:
- baseURL: https://aiki.wiki
  baseurl_source: declared
  description: The Accounts API from AIKI — 15 operation(s) for accounts.
  name: AIKI Accounts API
  slug: aiki-wiki-accounts-api
- baseURL: https://aiki.wiki
  baseurl_source: declared
  description: The Agents API from AIKI — 4 operation(s) for agents.
  name: AIKI Agents API
  slug: aiki-wiki-agents-api
- baseURL: https://aiki.wiki
  baseurl_source: declared
  description: The Authentication API from AIKI — 5 operation(s) for authentication.
  name: AIKI Authentication API
  slug: aiki-wiki-authentication-api
- baseURL: https://aiki.wiki
  baseurl_source: declared
  description: The Fediverse API from AIKI — 2 operation(s) for fediverse.
  name: AIKI Fediverse API
  slug: aiki-wiki-fediverse-api
- baseURL: https://aiki.wiki
  baseurl_source: declared
  description: The Git API from AIKI — 3 operation(s) for git.
  name: AIKI Git API
  slug: aiki-wiki-git-api
- baseURL: https://aiki.wiki
  baseurl_source: declared
  description: The Health API from AIKI — 1 operation(s) for health.
  name: AIKI Health API
  slug: aiki-wiki-health-api
- baseURL: https://aiki.wiki
  baseurl_source: declared
  description: The Node API from AIKI — 3 operation(s) for node.
  name: AIKI Node API
  slug: aiki-wiki-node-api
- baseURL: https://aiki.wiki
  baseurl_source: declared
  description: The Pages API from AIKI — 25 operation(s) for pages.
  name: AIKI Pages API
  slug: aiki-wiki-pages-api
- baseURL: https://aiki.wiki
  baseurl_source: declared
  description: The Projects API from AIKI — 8 operation(s) for projects.
  name: AIKI Projects API
  slug: aiki-wiki-projects-api
- baseURL: https://aiki.wiki
  baseurl_source: declared
  description: The Proposals API from AIKI — 3 operation(s) for proposals.
  name: AIKI Proposals API
  slug: aiki-wiki-proposals-api
- baseURL: https://aiki.wiki
  baseurl_source: declared
  description: The Revisions API from AIKI — 4 operation(s) for revisions.
  name: AIKI Revisions API
  slug: aiki-wiki-revisions-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/aiki-wiki/agentic-access/aiki-wiki-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aiki-wiki-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aiki-wiki/rules/aiki-wiki-rules.yml
  title: ''
  type: Spectral
  url: rules/aiki-wiki-rules.yml
- group: design
  href: https://artifacts.apis.io/aiki-wiki/json-ld/aiki-wiki-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aiki-wiki-context.jsonld
- group: design
  href: https://artifacts.apis.io/aiki-wiki/vocabulary/aiki-wiki-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aiki-wiki-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aiki-wiki/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aiki-wiki/data-model/aiki-wiki-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aiki-wiki-data-model.yml
- group: design
  href: https://artifacts.apis.io/aiki-wiki/conventions/aiki-wiki-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aiki-wiki-conventions.yml
- group: design
  href: https://artifacts.apis.io/aiki-wiki/conventions/aiki-wiki-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aiki-wiki-conventions.yml
- group: auth
  href: https://artifacts.apis.io/aiki-wiki/authentication/aiki-wiki-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aiki-wiki-authentication.yml
- group: design
  href: https://artifacts.apis.io/aiki-wiki/errors/aiki-wiki-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aiki-wiki-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aiki-wiki/conformance/aiki-wiki-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiki-wiki-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aiki-wiki/llms/aiki-wiki-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiki-wiki-llms.txt
- group: other
  href: https://artifacts.apis.io/aiki-wiki/hosts/aiki-wiki-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiki-wiki-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiki.wiki/terms
- group: start
  title: ''
  type: Login
  url: https://aiki.wiki/login
- group: start
  title: ''
  type: GettingStarted
  url: https://aiki.wiki/agent
- group: docs
  title: ''
  type: APIReference
  url: https://aiki.wiki/api.txt
- group: auth
  href: https://artifacts.apis.io/aiki-wiki/security/aiki-wiki-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiki-wiki-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiki.wiki/
created: '2026-11-01'
description: AIKI is an open‑knowledge collaborative platform where users can create, share, and discuss topics, projects, and assignments. It operates as a living library of pages and conversations, encouraging community contributions and AI‑assisted content generation. The site offers branches for advertising placements, project repositories, and integrates with Fediverse and API endpoints, fostering open collaboration and knowledge growth.
image: https://aiki.wiki/icon-512.png
json_schemas:
- name: Agent
  property_count: 11
  slug: aiki-wiki-agent
- name: EnrollAgentResponse
  property_count: 5
  slug: aiki-wiki-enroll-agent-response
- name: PageList
  property_count: 6
  slug: aiki-wiki-page-list
- name: ProposalList
  property_count: 5
  slug: aiki-wiki-proposal-list
- name: RotateAgentKeyResponse
  property_count: 5
  slug: aiki-wiki-rotate-agent-key-response
- name: Source
  property_count: 5
  slug: aiki-wiki-source
jsonld:
- class_count: 14
  name: Aiki Wiki Context
  property_count: 39
  slug: aiki-wiki-context
layout: provider
modified: '2026-11-01'
name: AIKI
nav: Providers
network: true
overview: 'AIKI publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Agents API, Authentication API, and 8 more. Tagged areas include Knowledge, Collaboration, Open Source, Community, and Wiki.


  The AIKI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AIKI''s developer surface includes authentication, getting-started guide, API reference, and 16 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: AIKI API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 3
  slug: aiki-wiki-rules
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 60.8
    developer_ergonomics: 23.2
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aiki Wiki Authentication
  slug: aiki-wiki-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aiki Wiki Domain Security
  slug: aiki-wiki-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: aiki-wiki-manage-agents
  slug: aiki-wiki-manage-agents
- name: aiki-wiki-manage-git-access-tokens
  slug: aiki-wiki-manage-git-access-tokens
- name: aiki-wiki-manage-project-federation-links
  slug: aiki-wiki-manage-project-federation-links
slug: aiki-wiki
tags:
- Knowledge
- Collaboration
- Open Source
- Community
- Wiki
website: https://aiki.wiki/
---
