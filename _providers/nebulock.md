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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 33
  human_in_the_loop: 1
  name: Nebulock Agentic Access
  operation_count: 55
  slug: nebulock-agentic-access
  summary_line: 55 operations · 33 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.nebulock.io
  baseurl_source: declared
  description: Actors, users, and hosts — the identity/asset correlation graph.
  name: Nebulock Entities API
  slug: nebulock-entities-api
- baseURL: https://api.nebulock.io
  baseurl_source: declared
  description: Retrieve and manage security findings and their comments.
  name: Nebulock Findings API
  slug: nebulock-findings-api
- baseURL: https://api.nebulock.io
  baseurl_source: declared
  description: Threat hunts, hunt suggestions, and hunt reports.
  name: Nebulock Hunts API
  slug: nebulock-hunts-api
- baseURL: https://api.nebulock.io
  baseurl_source: declared
  description: Create, validate, and run detection rules (Sigma / scheduled SQL).
  name: Nebulock Rules API
  slug: nebulock-rules-api
arazzos:
- description: Create a hunt, add a follow-up directive, then generate and fetch its report.
  name: Run a Nebulock hunt and generate a report
  slug: nebulock-run-hunt-and-report
- description: Validate rule content, create it inactive, then activate it.
  name: Validate and deploy a Nebulock detection rule
  slug: nebulock-validate-and-deploy-rule
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nebulock Public Entities API
  slug: open-nebulock-entities-api
- collection_type: open
  name: Nebulock Public Entities Findings API
  slug: open-nebulock-findings-api
- collection_type: open
  name: Nebulock Public Entities Hunts API
  slug: open-nebulock-hunts-api
- collection_type: open
  name: Nebulock Public Entities Rules API
  slug: open-nebulock-rules-api
common:
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nebulock.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nebulock.io/reference/getting-started-with-the-nebulock-findings-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nebulock.io/docs/access
- group: company
  title: ''
  type: Blog
  url: https://nebulock.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://nebulock.io/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nebulock
- group: operate
  title: ''
  type: Support
  url: https://docs.nebulock.io/docs/help
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.nebulock.io/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/nebulock-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nebulock-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nebulock-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nebulock-domain-security.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nebulock-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nebulock-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/nebulock-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nebulock-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nebulock-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nebulock-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nebulock-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nebulock-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nebulock-run-hunt-and-report.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nebulock-validate-and-deploy-rule.yml
- group: company
  title: ''
  type: Website
  url: https://nebulock.io/
created: '2026-07-17'
description: Nebulock is an agentic, contextual security-analytics platform built for hunt-first security operations. A swarm of AI agents continuously hunts across cloud, SaaS, network, endpoint, and identity telemetry, maintaining a behavioral Context Graph to surface endpoint- and identity-based threats, close detection coverage gaps, and catch human and agentic insider threats before they escalate into incidents. The platform runs hypothesis-driven investigations, writes and deploys detection rules (Sigma and scheduled SQL), retrohunts historical data, simulates attacks, and maps coverage against MITRE ATT&CK. Nebulock exposes a customer-facing public API for Findings, Entities (actors/users/hosts correlation), Hunts, hunt suggestions and reports, and detection Rules, authenticated with per-organization API keys. The company raised a $25M Series A and is backed by Bain Capital Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nebulock.png
layout: provider
modified: '2026-07-20'
name: Nebulock
nav: Providers
network: true
overview: 'Nebulock publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Entities API, Findings API, Hunts API, and 1 more. Tagged areas include Company, Security, Threat Hunting, Threat Detection, and Security Operations.


  Nebulock''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 18 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 4.5
    contract_quality: 54.3
    developer_ergonomics: 32.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 30.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nebulock/refs/heads/main/screenshots/nebulock-2026-08-07T184813.png
security:
- kind: authentication
  name: Nebulock Authentication
  slug: nebulock-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Nebulock Domain Security
  slug: nebulock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nebulock
tags:
- Company
- Security
- Threat Hunting
- Threat Detection
- Security Operations
- Detection Engineering
- AI Agents
- SIEM
website: https://nebulock.io/
---
