---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.6
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: A public, unauthenticated JSON API served by the Wand platform status page. It reports overall platform health, the four Wand products and the twenty-two production services behind them, plus thirty-d
  name: Wand Status API
  slug: status-api
- description: Wand runs Keycloak at auth.wand.ai as the identity provider for its platform. The master realm serves an anonymous OpenID Connect discovery document declaring the authorization, token, userinfo, intro
  name: Wand Identity (OpenID Connect)
  slug: identity
- description: The platform API behind Wand's Process Agentizer product, named "AI Workforce API" in Wand's own machine-readable status feed at https://status.wand.ai/api/services. The host api.wand.ai resolves insi
  name: Wand AI Workforce API
  slug: ai-workforce-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wand-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wand.ai/
- group: company
  title: ''
  type: Blog
  url: https://wand.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wand.ai/tc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wand.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wand-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wand1/
- group: company
  title: ''
  type: Careers
  url: https://wand.ai/careers
- group: operate
  title: ''
  type: ContactUs
  url: https://wand.ai/book-your-personalized-enterprise-ai-demo
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wand.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wand-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wand-ai-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/wand-ai-security.txt
- group: auth
  title: ''
  type: Security
  url: security/wand-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wand-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wand-ai-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wand-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wand-ai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wand-ai-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wand-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wand-ai-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wand-ai-vulnerability-disclosure.yml
created: '2026-09-04'
description: Wand (Wand Synthesis AI, Inc.) is a Palo Alto, California enterprise software company, founded in 2022 by Rotem Alaluf, that builds what it calls agentic labor infrastructure — an operating system for hybrid workforces in which AI agents are managed, executed and created as trusted team members alongside human employees. Its four published product areas are Process Agentizer (workforce automation, messaging and task orchestration), Collab (collaboration, chat and content ingestion), Governance (organization management and metrics) and Integration Hub (economy, billing and knowledge-vault integrations), offered on-premise, in a private cloud, or hosted. Wand publishes no developer portal, API reference or machine-readable contract; its platform API — named "AI Workforce API" in its own status feed — sits behind an enterprise sales gate at api.wand.ai. The public surfaces reached here are a JSON status API, a Keycloak OpenID Connect discovery document, a security.txt, and an llms.txt.
image: https://wand.ai/hubfs/logo.png
layout: provider
modified: '2026-09-04'
name: Wand
nav: Providers
network: true
overview: 'Wand publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Agentic AI, and Enterprise Software.


  Wand''s developer surface includes engineering blog, authentication, and 20 more developer resources.'
plans:
- name: Wand Ai Plans Pricing
  plan_count: 0
  slug: wand-ai-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Wand Ai Rate Limits
  slug: wand-ai-rate-limits
scopes:
- name: Wand Ai Scopes
  scope_count: 0
  slug: wand-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Wand Ai Authentication
  slug: wand-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Wand Ai Domain Security
  slug: wand-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wand Ai Vulnerability Disclosure
  slug: wand-ai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: wand-ai
tags:
- Company
- Artificial Intelligence
- AI Agents
- Agentic AI
- Enterprise Software
- Workforce Automation
- Orchestration
- Process Automation
- Collaboration
- Governance
website: https://wand.ai/
---
