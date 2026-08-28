---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Drift Com Agentic Access
  operation_count: 41
  slug: drift-com-agentic-access
  summary_line: 41 operations · 19 acting
api_count: 9
apis:
- description: The Accounts API from Drift — 4 operation(s) for accounts.
  name: Drift Accounts API
  slug: drift-com-accounts-api
- description: '[https://devdocs.drift.com/docs/app-uninstall](https://devdocs.drift.com/docs/app-uninstall)'
  name: Drift App Admin API
  slug: drift-com-app-admin-api
- description: '[https://devdocs.drift.com/docs/contact-model](https://devdocs.drift.com/docs/contact-model)'
  name: Drift Contacts API
  slug: drift-com-contacts-api
- description: '[https://devdocs.drift.com/docs/conversation-model](https://devdocs.drift.com/docs/conversation-model)'
  name: Drift Conversations and Messages API
  slug: drift-com-conversations-and-messages-api
- description: '[https://devdocs.drift.com/docs/automating-gdpr-retrieval-and-deletion](https://devdocs.drift.com/docs/automating-gdpr-retrieval-and-deletion)'
  name: Drift Data Privacy API
  slug: drift-com-data-privacy-api
- description: '[https://devdocs.drift.com/docs/playbook-model-1](https://devdocs.drift.com/docs/playbook-model-1)'
  name: Drift Playbooks API
  slug: drift-com-playbooks-api
- description: The SCIM API API from Drift — 2 operation(s) for scim api.
  name: Drift SCIM API API
  slug: drift-com-scim-api-api
- description: '[https://devdocs.drift.com/docs/team-model](https://devdocs.drift.com/docs/team-model)'
  name: Drift Teams API
  slug: drift-com-teams-api
- description: '[https://devdocs.drift.com/docs/user-model](https://devdocs.drift.com/docs/user-model)'
  name: Drift Users API
  slug: drift-com-users-api
artifact_total: 48
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Drift Accounts API
  slug: open-drift-com-accounts-api
- collection_type: open
  name: Drift Accounts App Admin API
  slug: open-drift-com-app-admin-api
- collection_type: open
  name: Drift Accounts Contacts API
  slug: open-drift-com-contacts-api
- collection_type: open
  name: Drift Accounts Conversations and Messages API
  slug: open-drift-com-conversations-and-messages-api
- collection_type: open
  name: Drift Accounts Data Privacy API
  slug: open-drift-com-data-privacy-api
- collection_type: open
  name: Drift Accounts Playbooks API
  slug: open-drift-com-playbooks-api
- collection_type: open
  name: Drift Accounts SCIM API API
  slug: open-drift-com-scim-api-api
- collection_type: open
  name: Drift Accounts Teams API
  slug: open-drift-com-teams-api
- collection_type: open
  name: Drift Accounts Users API
  slug: open-drift-com-users-api
- collection_type: open
  name: Drift
  slug: open-drift-com
- collection_type: open
  name: Drift
  slug: open-drift
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/drift-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drift-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/drift-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.drift.com/
- group: docs
  title: ''
  type: Documentation
  url: https://devdocs.drift.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://devdocs.drift.com/llms.txt
- group: start
  title: ''
  type: Portal
  url: https://app.drift.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Driftt
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Driftt/drift-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Driftt/drift-sdk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Driftt/drift-sdk-ios
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drift
- group: commercial
  title: ''
  type: Plans
  url: plans/drift-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/drift-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/drift-com-finops.yml
created: '2026-05-25'
description: Drift is a conversational marketing and sales platform delivering AI-powered chatbots, live chat, video messaging, account-based engagement, and Fastlane playbook automation on B2B websites. Drift was acquired by Salesloft in 2024 and now operates as the AI conversation surface within the Salesloft Revenue Orchestration Platform; the drift.com domain redirects to salesloft.com/platform/drift while devdocs.drift.com continues to host the developer API documentation.
features:
- description: Real-time, personalized AI conversations that engage website visitors and qualify leads.
  name: AI Chat Agent
- description: Form automation and conversational experiences that route qualified leads using tech-stack enrichment data.
  name: Fastlane Playbooks
- description: Human-handoff live chat tied into the rep workflow inside Salesloft Rhythm.
  name: Live Chat
- description: One-to-one and one-to-many video messages embedded in conversations and account workflows.
  name: Video Messaging
- description: Target accounts, route conversations to owners, and report on pipeline impact at the account level.
  name: Account-Based Engagement
- description: Realtime delivery of conversation, message, and contact events to subscribed endpoints.
  name: Webhooks
- description: SCIM 2.0 API for identity-provider-driven user provisioning and deprovisioning.
  name: SCIM Provisioning
- description: APIs to retrieve and delete personal data on request for GDPR compliance.
  name: GDPR Data Privacy
finops:
- name: Drift Com Finops
  service_category: Customer Support
  slug: drift-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drift-com.png
integrations:
- description: Native integration; Drift conversations flow into Salesloft Rhythm cadences and the Revenue Orchestration Platform.
  name: Salesloft
- description: Bi-directional sync of contacts, accounts, opportunities, and conversation activity.
  name: Salesforce
- description: Contact and conversation sync with HubSpot CRM and Marketing Hub.
  name: HubSpot
- description: Lead routing and program sync with Marketo Engage.
  name: Marketo
- description: Conversation notifications, routing, and rep response from Slack channels and DMs.
  name: Slack
json_structures:
- name: Drift Com Structure
  property_count: 0
  slug: drift-com-structure
layout: provider
modified: '2026-05-25'
name: Drift
nav: Providers
network: true
overview: 'Drift publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, App Admin API, Contacts API, and 6 more. Tagged areas include Conversational Marketing, Chatbots, Sales, Messaging, and Customer Engagement.


  Drift''s developer surface includes authentication, documentation, developer portal, and 12 more developer resources.'
plans:
- name: Drift Com Plans Pricing
  plan_count: 1
  slug: drift-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Drift Com Rate Limits
  slug: drift-com-rate-limits
score:
  band: thin
  composite: 32.0
  delta: 1.4
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 45.7
    developer_ergonomics: 44.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/drift-com/refs/heads/main/screenshots/drift-com-2026-06-20T180240.png
security:
- kind: authentication
  name: Drift Com Authentication
  slug: drift-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Drift Com Domain Security
  slug: drift-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: drift-com
solutions:
- description: Conversational marketing surface for demand-gen teams targeting B2B pipeline.
  name: Drift for Marketing
- description: Live chat plus video for AEs and SDRs running ABM and inbound motion.
  name: Drift for Sales
- description: Customer-facing chat for support and customer success teams.
  name: Drift for Service
tags:
- Conversational Marketing
- Chatbots
- Sales
- Messaging
- Customer Engagement
- Revenue Orchestration
- AI Chat
use_cases:
- description: Convert anonymous website visitors into qualified pipeline using AI chat plus Fastlane routing.
  name: Inbound Lead Qualification
- description: Route conversations from target accounts to the correct rep based on owner mapping and account hierarchy.
  name: ABM Conversation Routing
- description: Book qualified meetings directly into rep calendars from the chat surface.
  name: Meeting Booking
- description: Use chat and video to drive product adoption, renewal conversations, and customer success workflows.
  name: Post-Sale Customer Engagement
website: https://www.drift.com/
---
