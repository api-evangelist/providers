---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agentifai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agentifai.com/
- group: company
  title: ''
  type: Blog
  url: https://www.agentifai.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agentifai.com/legal/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.agentifai.com/talk-to-us
- group: company
  title: ''
  type: Careers
  url: https://careers.agentifai.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agentifaiofficial/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.agentifai.com/
- group: auth
  title: ''
  type: Compliance
  url: conformance/agentifai-conformance.yml
- group: auth
  title: ''
  type: Security
  url: security/agentifai-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agentifai-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/agentifai-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentifai-vulnerability-disclosure.yml
coverage:
  checked: '2026-09-12'
  detail: AgentifAI markets "Enterprise API Integration" and REST-based custom digital channels as AliceOS capabilities, but publishes no reference for them anywhere — no docs., api., developer. or app. subdomain resolves in DNS, /openapi.json and /api-docs return 404 on the only web host it runs, and the single published route to the platform is the "Talk to us" enterprise-demo form.
  evidence:
  - status: 200
    url: https://www.agentifai.com/talk-to-us
  - status: 404
    url: https://www.agentifai.com/openapi.json
  - status: 404
    url: https://www.agentifai.com/.well-known/api-catalog
  reason: sales-gate
  state: gated
created: '2026-09-12'
description: 'AgentifAI is a Portuguese enterprise conversational-AI company, headquartered in Braga, that builds AliceOS - a voice-first AI contact-center and autonomous agent platform purpose-built for the regulated banking and healthcare sectors. AliceOS is sold as a managed enterprise deployment rather than a self-serve developer product: it orchestrates multi-agent workflows across phone, WhatsApp, SMS, email and web, and integrates with core banking systems, CRMs, fraud engines, Hospital Information Systems and EMR/EHR platforms over REST, SOAP and OAuth, with SIP and CTI telephony adapters. Reference deployments include Santander, Banco BPI, Caixa Geral de Depositos, Vivalto Sante, Lusiadas Saude and Luz Saude. The company publishes a first-party llms.txt and a SafeBase trust center naming SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 42001:2023, PCI DSS v4.0.0 and HIPAA, but no public developer portal, API reference or machine-readable API contract.'
image: https://framerusercontent.com/assets/qpkeaKFM84CyDwOKMflAX4LCpI.webp
layout: provider
modified: '2026-09-12'
name: AgentifAI
nav: Providers
network: true
overview: 'AgentifAI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Conversational AI, Voice, and Contact Center.


  AgentifAI''s developer surface includes engineering blog and 12 more developer resources.'
plans:
- name: Agentifai Plans Pricing
  plan_count: 0
  slug: agentifai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Agentifai Rate Limits
  slug: agentifai-rate-limits
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    operational_transparency: 10.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 32.9
  schema_version: 0.22.0
  scored_at: '2026-09-12'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentifai Domain Security
  slug: agentifai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agentifai Vulnerability Disclosure
  slug: agentifai-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Agentifai Trust Center
  slug: agentifai-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 42001:2023, PCI DSS v4.0.0, HIPAA
slug: agentifai
tags:
- Company
- Artificial Intelligence
- Conversational AI
- Voice
- Contact Center
- Banking
- Healthcare
- Agents
- Portugal
website: https://www.agentifai.com/
---
