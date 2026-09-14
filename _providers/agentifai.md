---
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
