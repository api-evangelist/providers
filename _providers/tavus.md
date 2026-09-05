---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Tavus Agentic Access
  operation_count: 54
  slug: tavus-agentic-access
  summary_line: 54 operations · 31 acting
api_count: 1
apis:
- description: The Tavus REST API powers personalized video generation and real-time Conversational Video Interface sessions. It exposes endpoints for replicas (Phoenix-4 video and image-to-replica), async video gen
  name: Tavus API
  slug: tavus-api
- baseURL: https://tavusapi.com
  baseurl_source: declared
  description: The Conversations API from Tavus — 3 operation(s) for conversations.
  name: Tavus Conversations API
  slug: tavus-conversations-api
- baseURL: https://tavusapi.com
  baseurl_source: declared
  description: The Documents API from Tavus — 3 operation(s) for documents.
  name: Tavus Documents API
  slug: tavus-documents-api
- baseURL: https://tavusapi.com
  baseurl_source: declared
  description: The Guardrails API from Tavus — 2 operation(s) for guardrails.
  name: Tavus Guardrails API
  slug: tavus-guardrails-api
- baseURL: https://tavusapi.com
  baseurl_source: declared
  description: The Lipsync API from Tavus — 2 operation(s) for lipsync.
  name: Tavus Lipsync API
  slug: tavus-lipsync-api
- baseURL: https://tavusapi.com
  baseurl_source: declared
  description: The Objectives API from Tavus — 2 operation(s) for objectives.
  name: Tavus Objectives API
  slug: tavus-objectives-api
- baseURL: https://tavusapi.com
  baseurl_source: declared
  description: The Personas API from Tavus — 2 operation(s) for personas.
  name: Tavus Personas API
  slug: tavus-personas-api
- baseURL: https://tavusapi.com
  baseurl_source: declared
  description: The Pronunciation Dictionaries API from Tavus — 2 operation(s) for pronunciation dictionaries.
  name: Tavus Pronunciation Dictionaries API
  slug: tavus-pronunciation-dictionaries-api
- baseURL: https://tavusapi.com
  baseurl_source: declared
  description: The Replacements API from Tavus — 2 operation(s) for replacements.
  name: Tavus Replacements API
  slug: tavus-replacements-api
- baseURL: https://tavusapi.com
  baseurl_source: declared
  description: The Replicas API from Tavus — 3 operation(s) for replicas.
  name: Tavus Replicas API
  slug: tavus-replicas-api
- baseURL: https://tavusapi.com
  baseurl_source: declared
  description: The Transcriptions API from Tavus — 2 operation(s) for transcriptions.
  name: Tavus Transcriptions API
  slug: tavus-transcriptions-api
- baseURL: https://tavusapi.com
  baseurl_source: declared
  description: The Videos API from Tavus — 3 operation(s) for videos.
  name: Tavus Videos API
  slug: tavus-videos-api
- baseURL: https://tavusapi.com
  baseurl_source: declared
  description: The Voices API from Tavus — 1 operation(s) for voices.
  name: Tavus Voices API
  slug: tavus-voices-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tavus Developer API Collection Conversations API
  slug: open-tavus-conversations-api
- collection_type: open
  name: Tavus Developer API Collection Conversations Documents API
  slug: open-tavus-documents-api
- collection_type: open
  name: Tavus Developer API Collection Conversations Guardrails API
  slug: open-tavus-guardrails-api
- collection_type: open
  name: Tavus Developer API Collection Conversations Lipsync API
  slug: open-tavus-lipsync-api
- collection_type: open
  name: Tavus Developer API Collection Conversations Objectives API
  slug: open-tavus-objectives-api
- collection_type: open
  name: Tavus Developer API Collection Conversations Personas API
  slug: open-tavus-personas-api
- collection_type: open
  name: Tavus Developer API Collection Conversations Pronunciation Dictionaries API
  slug: open-tavus-pronunciation-dictionaries-api
- collection_type: open
  name: Tavus Developer API Collection Conversations Replacements API
  slug: open-tavus-replacements-api
- collection_type: open
  name: Tavus Developer API Collection Conversations Replicas API
  slug: open-tavus-replicas-api
- collection_type: open
  name: Tavus Developer API Collection Conversations Transcriptions API
  slug: open-tavus-transcriptions-api
- collection_type: open
  name: Tavus Developer API Collection Conversations Videos API
  slug: open-tavus-videos-api
- collection_type: open
  name: Tavus Developer API Collection Conversations Voices API
  slug: open-tavus-voices-api
- collection_type: open
  name: Tavus Developer API Collection
  slug: open-tavus
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tavus-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tavus-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tavus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tavus-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tavus.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tavus.io
- group: company
  title: ''
  type: Blog
  url: https://www.tavus.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tavus-Engineering
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tavus.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tavus.io/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tavus.io/legal/privacy-policy
- group: other
  title: ''
  type: X
  url: https://x.com/heyTavus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tavus
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.tavus.io/changelog
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.tavus.io/llms.txt
created: '2026-05-23'
description: Tavus builds the Conversational Video Interface (CVI), an end-to-end pipeline that combines AI behavior with lifelike digital humans for real-time video conversations. The platform lets developers create personal AI replicas from a short video or a single image (Phoenix-4 and image-to-replica), generate async personalized videos, and run real-time conversational sessions backed by configurable personas, custom LLMs, tools, and document knowledge bases. Tavus targets product teams embedding human-like AI into sales, support, healthcare, education, and recruiting experiences, and monetizes through usage-based developer pricing and enterprise contracts.
finops:
- name: Tavus Finops
  service_category: API
  slug: tavus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tavus.png
layout: provider
modified: '2026-05-23'
name: Tavus
nav: Providers
network: true
overview: 'Tavus publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Conversations API, Documents API, Guardrails API, and 9 more. Tagged areas include Artificial Intelligence, Generative AI, Video, Conversational AI, and Avatars.


  Tavus'' developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 10 more developer resources.'
plans:
- name: Tavus Plans Pricing
  plan_count: 1
  slug: tavus-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Tavus Rate Limits
  slug: tavus-rate-limits
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 58.6
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tavus/refs/heads/main/screenshots/tavus-2026-06-20T194933.png
security:
- kind: authentication
  name: Tavus Authentication
  slug: tavus-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tavus Domain Security
  slug: tavus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tavus Trust Center
  slug: tavus-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: tavus
tags:
- Artificial Intelligence
- Generative AI
- Video
- Conversational AI
- Avatars
- Replicas
- Personalization
- Real-Time
- CVI
- Webhook
website: https://www.tavus.io
---
