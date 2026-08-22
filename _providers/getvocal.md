---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Getvocal Agentic Access
  operation_count: 3
  slug: getvocal-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: The Contact API from GetVocal — 1 operation(s) for contact.
  name: GetVocal Contact API
  slug: getvocal-contact-api
- description: The Llms.txt API from GetVocal — 1 operation(s) for llms.txt.
  name: GetVocal Llms.txt API
  slug: getvocal-llms-txt-api
- description: The .well Known API from GetVocal — 1 operation(s) for .well known.
  name: GetVocal .well Known API
  slug: getvocal-well-known-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GetVocal Agent Contact API
  slug: open-getvocal-contact-api
- collection_type: open
  name: GetVocal Agent Contact Llms.txt API
  slug: open-getvocal-llms-txt-api
- collection_type: open
  name: GetVocal Agent Contact .well Known API
  slug: open-getvocal-well-known-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/getvocal-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/getvocal-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/getvocal-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/getvocal-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/getvocal-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/getvocal-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/getvocal-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.getvocal.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/getvocal-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getvocal-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.getvocal.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.getvocal.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getvocal
- group: start
  title: ''
  type: SignUp
  url: https://www.getvocal.ai/contact/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getvocal.ai/legal-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getvocal.ai/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.getvocal.ai/
created: '2026-07-17'
description: GetVocal builds AI voice and chat agents for regulated, high-volume customer operations. Its agents resolve customer conversations end to end while staying inside a business's own rules, with human-in-the-loop approval on high-stakes actions such as large transactions, high-value returns and sensitive data. Products include Agent Builder, Control Tower and a Hybrid Workplace Platform, serving telecom, financial services, retail and e-commerce, BPO, healthcare and hospitality across 100+ languages. GetVocal ships an agent-native surface — a public OpenAPI, an llms.txt guidance file, an ai-plugin manifest and a WebMCP tool server — with on-premises, self-hosted, EU-hosted or hybrid deployment. Backed by Creandum and Speedinvest.
image: https://www.getvocal.ai/getvocal-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: getvocal-mcp.yml
  slug: getvocal-mcpyml
modified: '2026-07-19'
name: GetVocal
nav: Providers
network: true
overview: 'GetVocal publishes 3 APIs on the [APIs.io](https://apis.io/) network: Contact API, Llms.txt API, and .well Known API. Tagged areas include Company, Ai, Voice AI, Conversational AI, and Customer Experience.


  GetVocal''s developer surface includes documentation, engineering blog, signup flow, and 15 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 36.0
  delta: -3.2
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 30.3
    contract_quality: 51.0
    developer_ergonomics: 13.7
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 2.6
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getvocal/refs/heads/main/screenshots/getvocal-2026-07-25T215750.png
security:
- kind: domain-security
  name: Getvocal Domain Security
  slug: getvocal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Getvocal Trust Center
  slug: getvocal-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: getvocal
tags:
- Company
- Ai
- Voice AI
- Conversational AI
- Customer Experience
- AI Agents
- Contact Center
- Agent Governance
- MCP
- Agent Native
website: https://www.getvocal.ai/
---
