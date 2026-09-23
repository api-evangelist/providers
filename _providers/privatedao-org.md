---
agent_readiness:
  band: agent-ready
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-09-23'
api_count: 2
apis:
- baseURL: https://agents.privatedao.org
  baseurl_source: declared
  description: 'Machine-native verification, evidence and agent-workflow services on Solana mainnet. Discover services, create jobs (two free, twelve paid per job in USDC with a quote-first 402 payment_intent flow), '
  name: PrivateDAO Agent Exchange API
  slug: agent-exchange-api
- baseURL: https://api.privatedao.org/api/v1
  baseurl_source: declared
  description: Prove that a private policy (e.g. a credit-capacity rule over private records, risk score and liabilities) was satisfied without revealing the inputs. Groth16 proofs over the private_dao_blind_policy_
  name: PrivateDAO Blind Policy Verification API
  slug: blind-policy-verification-api
artifact_total: 9
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/security/privatedao-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/privatedao-org-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/security/privatedao-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/privatedao-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://privatedao.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://privatedao.org/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://privatedao.org/llms-full.txt
- group: docs
  title: ''
  type: APIReference
  url: https://privatedao.org/developers/blind-policy-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://agents.privatedao.org/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/llms/privatedao-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/privatedao-org-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://privatedao.org/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/llms/privatedao-org-agents-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/privatedao-org-agents-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/a2a/privatedao-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/privatedao-org-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/mcp/privatedao-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/privatedao-org-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/mcp/privatedao-org-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/privatedao-org-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/well-known/privatedao-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/privatedao-org-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/well-known/privatedao-org-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/privatedao-org-security.txt
- group: auth
  title: ''
  type: Security
  url: https://privatedao.org/security/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/conformance/privatedao-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/privatedao-org-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/errors/privatedao-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/privatedao-org-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/lifecycle/privatedao-org-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/privatedao-org-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/authentication/privatedao-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/privatedao-org-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/conventions/privatedao-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/privatedao-org-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/sandbox/privatedao-org-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/privatedao-org-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/plans/privatedao-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/privatedao-org-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/rate-limits/privatedao-org-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/privatedao-org-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/packages/privatedao-org-packages.yml
  title: ''
  type: Packages
  url: packages/privatedao-org-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/data-model/privatedao-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/privatedao-org-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/overlays/privatedao-org-agent-exchange-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/privatedao-org-agent-exchange-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/privatedao-org/refs/heads/main/overlays/privatedao-org-blind-policy-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/privatedao-org-blind-policy-overlay.yaml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/X-PACT
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/X-PACT/PrivateDAO-public
- group: operate
  title: ''
  type: Roadmap
  url: https://privatedao.org/roadmap/
- group: operate
  title: ''
  type: Support
  url: https://privatedao.org/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://privatedao.org/legal/
- group: docs
  title: ''
  type: Documentation
  url: https://privatedao.org/whitepaper/
- group: other
  title: ''
  type: X
  url: https://x.com/privateDAOOS
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/dpD5c7Gfcc
- group: other
  title: ''
  type: Telegram
  url: https://t.me/privateDAOOS
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@privatedao
created: '2026-09-19'
description: 'PrivateDAO (X-PACT) sells privacy-and-proof infrastructure for organizations: confidential payroll, treasury coordination, private governance, sealed auctions and blind/record verification that keep the underlying data private while producing a verifiable outcome. Two public APIs are published: the Agent Exchange on agents.privatedao.org (an unauthenticated, pay-per-job USDC-on-Solana service marketplace exposed over REST, a live A2A agent and a hosted MCP server) and the Blind Policy Verification API on api.privatedao.org (Groth16 zero-knowledge proofs that a private policy was satisfied).'
image: https://privatedao.org/assets/privatedao-brand-mark-20260918.jpeg
layout: provider
mcp_servers:
- description: ''
  name: PrivateDAO MCP Server
  slug: privatedao-mcp-server
- description: ''
  name: Hosted MCP endpoint
  slug: hosted-mcp-endpoint
modified: '2026-09-19'
name: PrivateDAO
nav: Providers
network: true
overview: 'PrivateDAO publishes 2 APIs on the [APIs.io](https://apis.io/) network: Agent Exchange API and Blind Policy Verification API. Tagged areas include Company, Agents, A2A, MCP, and Verification.


  PrivateDAO''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, support, YouTube channel, and 32 more developer resources.'
plans:
- name: Privatedao Org Plans Pricing
  plan_count: 21
  slug: privatedao-org-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Privatedao Org Rate Limits
  slug: privatedao-org-rate-limits
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 38.4
    developer_ergonomics: 63.7
    discoverability: 75.9
    operational_transparency: 21.1
  previous_composite: 44.5
  provenance:
    conformance: derived
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
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Privatedao Org Authentication
  slug: privatedao-org-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Privatedao Org Domain Security
  slug: privatedao-org-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Privatedao Org Vulnerability Disclosure
  slug: privatedao-org-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: privatedao-org
tags:
- Company
- Agents
- A2A
- MCP
- Verification
- Zero-Knowledge Proofs
- Solana
- Blockchain
- Payments
- Marketplace
- Privacy
- Governance
- Treasury
website: https://privatedao.org/
---
