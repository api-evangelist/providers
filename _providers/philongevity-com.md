---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-09-25'
api_count: 2
apis:
- description: Official Model Context Protocol server for the PRISM biomarker-analysis engine. Hosted Streamable HTTP at https://philongevity.com/mcp (6 tools — analyze_biomarkers, list_supported_biomarkers, quick_c
  name: Phi Longevity PRISM MCP Server
  slug: phi-longevity-prism-mcp-server
- description: A2A 1.0 agent (JSON-RPC at https://philongevity.com/a2a) with one skill — chronic-disease records consolidation and visit prep — described by an ES256-signed agent card at /.well-known/agent-card.json
  name: Phi Longevity PRISM A2A Agent
  slug: phi-longevity-prism-a2a-agent
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://philongevity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://philongevity.com/for-agents
- group: docs
  title: ''
  type: Documentation
  url: https://philongevity.com/for-agents
- group: start
  title: ''
  type: GettingStarted
  url: https://philongevity.com/for-agents
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Philongevity
- group: company
  title: ''
  type: Blog
  url: https://philongevity.com/blog
- group: operate
  title: ''
  type: FAQ
  url: https://philongevity.com/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://philongevity.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://philongevity.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://philongevity.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://philongevity.com/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/security/philongevity-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/philongevity-com-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://philongevity.com/trust
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/llms/philongevity-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/philongevity-com-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/a2a/philongevity-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/philongevity-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/mcp/philongevity-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/philongevity-com-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/well-known/philongevity-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/philongevity-com-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/packages/philongevity-com-packages.yml
  title: ''
  type: Packages
  url: packages/philongevity-com-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/conformance/philongevity-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/philongevity-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/errors/philongevity-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/philongevity-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/lifecycle/philongevity-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/philongevity-com-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/authentication/philongevity-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/philongevity-com-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/security/philongevity-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/philongevity-com-domain-security.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/sandbox/philongevity-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/philongevity-com-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/conventions/philongevity-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/philongevity-com-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/changelog/philongevity-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/philongevity-com-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/components/philongevity-com-components.yml
  title: ''
  type: Components
  url: components/philongevity-com-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/plans/philongevity-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/philongevity-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/rate-limits/philongevity-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/philongevity-com-rate-limits.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/philongevity-com/refs/heads/main/regulatory/philongevity-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/philongevity-com-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://philongevity.com/privacy
- group: other
  title: ''
  type: ExitAssistance
  url: https://philongevity.com/trust
- group: other
  title: ''
  type: Subprocessors
  url: https://philongevity.com/privacy
- group: other
  title: ''
  type: AITransparency
  url: https://philongevity.com/trust
created: '2026-09-19'
description: 'Phi Longevity is a US health-data intelligence company whose PRISM engine consolidates a person''s lab reports, wearable data and clinical notes into one scored, guideline-cited health report, with condition tracks for type-2 diabetes, lupus, cancer survivorship and general wellness. Its public developer surface is agent-native rather than REST: an official MCP server (hosted Streamable HTTP endpoint plus an npm stdio package, six tools, no key required, synthetic or de-identified values only), a signed A2A 1.0 agent card with an AP2/x402 pay-per-use extension, an llms.txt, and a $4.99 USDC per-call paid report settled via x402 on Base. Real medical records are analyzed only inside the authenticated app under a Google Cloud HIPAA BAA — PHI never transits the agent surfaces.'
image: https://philongevity.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Phi Longevity MCP Server
  slug: phi-longevity-mcp-server
modified: '2026-09-19'
name: Phi Longevity
nav: Providers
network: true
overview: 'Phi Longevity publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Data, Lab Results, and Biomarkers.


  Phi Longevity''s developer surface includes documentation, getting-started guide, engineering blog, FAQ, pricing, signup flow, authentication, and 28 more developer resources.'
plans:
- name: Philongevity Com Plans Pricing
  plan_count: 3
  slug: philongevity-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Philongevity Com Rate Limits
  slug: philongevity-com-rate-limits
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.2
    discoverability: 75.0
    operational_transparency: 21.1
  previous_composite: 44.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 33.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Philongevity Com Authentication
  slug: philongevity-com-authentication
  summary_line: none · 4 schemes
- kind: domain-security
  name: Philongevity Com Domain Security
  slug: philongevity-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Philongevity Com Trust Center
  slug: philongevity-com-trust-center
  summary_line: trust center published
slug: philongevity-com
tags:
- Company
- Healthcare
- Health Data
- Lab Results
- Biomarkers
- Chronic Disease
- Longevity
- MCP
- A2A
- Agentic Payments
- x402
- Artificial Intelligence
website: https://philongevity.com/
---
