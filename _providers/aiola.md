---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 14.2
  scored_at: '2026-09-20'
api_count: 3
apis:
- description: 'Jargonic automatic speech recognition. Batch file transcription over HTTP (POST /api/speech-to-text/file, 50 MB maximum file size) and real-time streaming transcription over a Socket.IO connection at '
  name: aiOla Speech to Text API
  slug: aiola-speech-to-text
- description: Low-latency speech synthesis with multi-language, multi-voice support and jargon-pronunciation conditioning. Batch synthesis (POST /api/tts/synthesize) and chunked streaming synthesis (POST /api/tts/s
  name: aiOla Text to Speech API
  slug: aiola-text-to-speech
- description: Two-tier authentication service. An API key is exchanged for a short-lived bearer token (POST /voip-auth/apiKey2Token), which is then exchanged for a session JWT access token scoped to a workflow (POS
  name: aiOla Authentication API
  slug: aiola-auth
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://aiola.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aiola.ai/get-started/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aiola.ai/get-started/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aiola.ai/get-started/quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiola/refs/heads/main/authentication/aiola-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aiola-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://customer.support.aiola.com/servicedesk/customer/portals
- group: company
  title: ''
  type: Blog
  url: https://aiola.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aiola-lab
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiola.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiola.ai/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aiola.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.aiola.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiola/refs/heads/main/security/aiola-trust-center.yml
  title: ''
  type: Compliance
  url: security/aiola-trust-center.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aiola/refs/heads/main/packages/aiola-packages.yml
  title: ''
  type: Packages
  url: packages/aiola-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aiola/refs/heads/main/packages/aiola-packages.yml
  title: ''
  type: SDKs
  url: packages/aiola-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiola/refs/heads/main/mcp/aiola-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aiola-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiola/refs/heads/main/llms/aiola-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiola-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiola/refs/heads/main/lifecycle/aiola-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aiola-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiola/refs/heads/main/conventions/aiola-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aiola-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiola/refs/heads/main/errors/aiola-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/aiola-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiola/refs/heads/main/conformance/aiola-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiola-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aiola/refs/heads/main/rate-limits/aiola-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aiola-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aiola/refs/heads/main/plans/aiola-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiola-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiola/refs/heads/main/security/aiola-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiola-domain-security.yml
created: '2026-09-14'
description: 'aiOla is a deep-tech voice, speech and conversational AI lab that sells enterprise Speech AI as an API: the Jargonic family of multilingual automatic speech recognition models (Jargonic-v2, Jargonic-v2-Flash, Jargonic-v1) with zero-shot jargon and keyword spotting, a low-latency text-to-speech model with jargon-pronunciation conditioning, and a speech-understanding layer covering summarization, sentiment, entity, topic and key-phrase detection, auto chapters, content moderation and PII redaction. The developer surface is delivered through first-party Python, JavaScript/TypeScript, C# and Swift SDKs against a REST + Socket.IO API, with a two-tier API-key-to-JWT authentication model. The company also packages the same technology as field voice agents that capture data into Salesforce for enterprise field teams.'
image: https://aiola.ai/wp-content/uploads/2026/03/favicon-300x300.png
layout: provider
mcp_servers:
- description: ''
  name: aiOla Documentation MCP Server
  slug: aiola-documentation-mcp-server
modified: '2026-09-14'
name: aiOla
nav: Providers
network: true
overview: 'aiOla publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Speech Recognition, Speech-to-Text, Text-to-Speech, Voice AI, and Conversational AI.


  aiOla''s developer surface includes documentation, getting-started guide, authentication, support, engineering blog, and 19 more developer resources.'
plans:
- name: Aiola Plans Pricing
  plan_count: 0
  slug: aiola-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Aiola Rate Limits
  slug: aiola-rate-limits
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 81.5
    operational_transparency: 18.4
  previous_composite: 29.7
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aiola Authentication
  slug: aiola-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aiola Domain Security
  slug: aiola-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aiola Vulnerability Disclosure
  slug: aiola-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Aiola Trust Center
  slug: aiola-trust-center
  summary_line: SOC 2 Type II, ISO 27001:2022
slug: aiola
tags:
- Speech Recognition
- Speech-to-Text
- Text-to-Speech
- Voice AI
- Conversational AI
- Artificial Intelligence
- Machine-Learning
- Audio
- Transcription
- Enterprise
website: https://aiola.ai/
---
