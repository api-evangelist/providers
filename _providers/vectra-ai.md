---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Vectra AI Platform REST API (api.vectra.io) provides programmatic access to detections, hosts, accounts, assignments, threat-intelligence indicators, and platform configuration for the Vectra AI P
  name: Vectra AI Platform API
  slug: vectra-ai-platform-api
artifact_total: 26
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/vectra-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vectra-ai-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vectra-networks
- group: company
  title: ''
  type: Website
  url: https://www.vectra.ai/
- group: start
  title: Vectra AI Customer Support Portal
  type: Portal
  url: https://support.vectra.ai
- group: docs
  title: ''
  type: Documentation
  url: https://support.vectra.ai
- group: company
  title: ''
  type: Blog
  url: https://www.vectra.ai/blog
- group: other
  title: ''
  type: Resources
  url: https://www.vectra.ai/resources
- group: operate
  title: ''
  type: ContactSales
  url: https://www.vectra.ai/contact
- group: company
  title: ''
  type: Careers
  url: https://www.vectra.ai/company/careers
- group: company
  title: ''
  type: Partners
  url: https://www.vectra.ai/partners
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vectra.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vectra.ai/terms
created: '2026-05-23'
description: Vectra AI is an AI-driven network detection and response (NDR) vendor whose Vectra AI Platform applies Attack Signal Intelligence across network, cloud, identity, Microsoft 365, Entra ID, AWS, Azure, Google Cloud, and IoT/OT environments. The platform combines 150+ AI models and 39 AI patents to surface attacker behavior at scale, and is offered with optional Managed Extended Detection and Response (MXDR) services. Vectra exposes a gated REST API at api.vectra.io for partner and customer integrations with SIEMs, SOARs, EDR tools, and ticketing systems. Named a Leader in the 2026 Gartner Magic Quadrant for NDR.
features:
- description: Vectra's AI engine using 150+ AI models and 39 AI patents to surface real attacker behavior
  name: Attack Signal Intelligence
- description: NDR coverage across data center, campus, remote, cloud, and IoT/OT environments
  name: Network Detection
- description: Detections across AWS, Azure, and Google Cloud control-plane and workload signals
  name: Cloud Detection
- description: Detections across Microsoft 365, Entra ID, and other identity providers
  name: Identity Detection
- description: Optional 24x7x365 Managed Extended Detection and Response service delivered by Vectra analysts
  name: MXDR
- description: Investigation workflows surfacing host, account, and detection context for SOC analysts
  name: Threat Investigation
- description: AI-based prioritization that reduces alert noise and surfaces the highest-risk threats
  name: AI-Driven Triage
finops:
- name: Vectra Ai Finops
  service_category: API
  slug: vectra-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vectra-ai.png
integrations:
- description: SIEM integration for streaming detections, hosts, and accounts into Splunk
  name: Splunk
- description: Native integration with Microsoft Sentinel for cloud-native SIEM workflows
  name: Microsoft Sentinel
- description: Integration for forwarding Vectra detections into Google Chronicle
  name: Google Chronicle
- description: Playbook content and connectors for Palo Alto Cortex XSOAR
  name: Cortex XSOAR
- description: Bidirectional integration with Splunk SOAR for automated response
  name: Splunk SOAR
- description: Cross-correlation and response integration with CrowdStrike Falcon
  name: CrowdStrike
- description: Integration with Microsoft Defender for endpoint context and response
  name: Microsoft Defender
- description: Endpoint integration with SentinelOne for cross-tool detection and response
  name: SentinelOne
layout: provider
modified: '2026-05-23'
name: Vectra AI
nav: Providers
network: true
overview: 'Vectra AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, NDR, XDR, AI Detection, and Network Security.


  Vectra AI''s developer surface includes developer portal, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Vectra Ai Plans Pricing
  plan_count: 1
  slug: vectra-ai-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Vectra Ai Rate Limits
  slug: vectra-ai-rate-limits
score:
  band: emerging
  composite: 21.2
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vectra-ai/refs/heads/main/screenshots/vectra-ai-2026-06-20T200847.png
security:
- kind: domain-security
  name: Vectra Ai Domain Security
  slug: vectra-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vectra Ai Trust Center
  slug: vectra-ai-trust-center
  summary_line: SOC 2, ISO 27001
slug: vectra-ai
tags:
- Cybersecurity
- NDR
- XDR
- AI Detection
- Network Security
- Cloud Security
- MXDR
use_cases:
- description: Detect lateral movement across data center, cloud, and remote networks
  name: NDR for Hybrid Networks
- description: Detect credential abuse, privilege escalation, and account compromise across hybrid environments
  name: Cloud and Identity Threat Detection
- description: Use Attack Signal Intelligence to compress alert volume into high-fidelity threats
  name: SOC Alert Reduction
- description: Offload 24x7 detection and response to the Vectra MXDR team
  name: Managed XDR
- description: Detect ransomware behaviors across network, identity, and cloud surfaces before encryption
  name: Ransomware Defense
website: https://www.vectra.ai/
---
