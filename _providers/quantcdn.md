---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 125
  human_in_the_loop: 10
  name: Quantcdn Agentic Access
  operation_count: 226
  slug: quantcdn-agentic-access
  summary_line: 226 operations · 125 acting · 10 human-in-the-loop
api_count: 38
apis:
- description: Pre-configured AI assistants with specific system prompts, model settings, and tool permissions
  name: QuantCDN AI Agents API
  slug: quantcdn-ai-agents-api
- description: Custom tool definitions for AI function calling
  name: QuantCDN AI Custom Tools API
  slug: quantcdn-ai-custom-tools-api
- description: S3-backed file storage for AI workloads
  name: QuantCDN AI File Storage API
  slug: quantcdn-ai-file-storage-api
- description: AI Filter Policies
  name: QuantCDN AI Filter Policies API
  slug: quantcdn-ai-filter-policies-api
- description: AI Governance
  name: QuantCDN AI Governance API
  slug: quantcdn-ai-governance-api
- description: Chat inference, embeddings, and image generation services
  name: QuantCDN AI Inference API
  slug: quantcdn-ai-inference-api
- description: Foundation model listing and configuration
  name: QuantCDN AI Models API
  slug: quantcdn-ai-models-api
- description: Usage statistics and monitoring for AI services
  name: QuantCDN AI Monitoring API
  slug: quantcdn-ai-monitoring-api
- description: Durable batch processing orchestrations with pause/resume support
  name: QuantCDN AI Orchestrations API
  slug: quantcdn-ai-orchestrations-api
- description: Conversation session management for multi-turn interactions
  name: QuantCDN AI Sessions API
  slug: quantcdn-ai-sessions-api
- description: Reusable prompts, workflows, and instructions for agents
  name: QuantCDN AI Skills API
  slug: quantcdn-ai-skills-api
- description: AI Slack Bots
  name: QuantCDN AI Slack Bots API
  slug: quantcdn-ai-slack-bots-api
- description: Multi-agent task coordination and dependency management
  name: QuantCDN AI Task Management API
  slug: quantcdn-ai-task-management-api
- description: Built-in tool listing and async tool execution polling
  name: QuantCDN AI Tools API
  slug: quantcdn-ai-tools-api
- description: AI Usage
  name: QuantCDN AI Usage API
  slug: quantcdn-ai-usage-api
- description: Vector database collections for RAG and semantic search
  name: QuantCDN AI Vector Database API
  slug: quantcdn-ai-vector-database-api
- description: Cloud application lifecycle management
  name: QuantCDN Applications API
  slug: quantcdn-applications-api
- description: Backup and restore operations for applications
  name: QuantCDN Backup Management API
  slug: quantcdn-backup-management-api
- description: CDN traffic metrics and analytics
  name: QuantCDN CDN Metrics API
  slug: quantcdn-cdn-metrics-api
- description: Execute commands in application containers
  name: QuantCDN Commands API
  slug: quantcdn-commands-api
- description: Docker compose configuration management
  name: QuantCDN Compose API
  slug: quantcdn-compose-api
- description: Container management and operations
  name: QuantCDN Containers API
  slug: quantcdn-containers-api
- description: Website crawler configuration and management
  name: QuantCDN Crawlers API
  slug: quantcdn-crawlers-api
- description: Scheduled website crawl operations
  name: QuantCDN CrawlerSchedules API
  slug: quantcdn-crawlerschedules-api
- description: Scheduled task management
  name: QuantCDN Cron API
  slug: quantcdn-cron-api
- description: Domain and DNS management
  name: QuantCDN Domains API
  slug: quantcdn-domains-api
- description: Application environment management and configuration
  name: QuantCDN Environments API
  slug: quantcdn-environments-api
- description: HTTP header rule management
  name: QuantCDN Headers API
  slug: quantcdn-headers-api
- description: Key-value store operations
  name: QuantCDN KV API
  slug: quantcdn-kv-api
- description: Organization management and settings
  name: QuantCDN Organizations API
  slug: quantcdn-organizations-api
- description: Static site project management
  name: QuantCDN Projects API
  slug: quantcdn-projects-api
- description: Cache purging and invalidation
  name: QuantCDN Purge API
  slug: quantcdn-purge-api
- description: Edge rules (redirects, authentication, proxies, etc.)
  name: QuantCDN Rules API
  slug: quantcdn-rules-api
- description: Auto-scaling policies and configuration
  name: QuantCDN ScalingPolicy API
  slug: quantcdn-scalingpolicy-api
- description: SSH key management for container access
  name: QuantCDN SSH Access API
  slug: quantcdn-ssh-access-api
- description: API token management
  name: QuantCDN Tokens API
  slug: quantcdn-tokens-api
- description: Environment variable management
  name: QuantCDN Variables API
  slug: quantcdn-variables-api
- description: Persistent storage volume management
  name: QuantCDN Volumes API
  slug: quantcdn-volumes-api
artifact_total: 46
collections:
- collection_type: open
  name: QuantCDN API
  slug: open-quantcdn
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quantcdn-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/quantcdn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quantcdn-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quantcdn-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quantcdn
- group: company
  title: ''
  type: Website
  url: https://www.quantcdn.io/home
- group: docs
  title: ''
  type: Documentation
  url: https://docs.quantcdn.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quantcdn
- group: company
  title: ''
  type: Blog
  url: https://www.quantcdn.io/blog
created: '2025-02-12'
description: QuantCDN is an edge delivery, static site hosting, and cloud applications platform that lets teams generate, host, and maintain static and dynamic versions of their websites with a global CDN, WAF, edge functions, key-value storage, AI inference, and DNS management.
finops:
- name: Quantcdn Finops
  service_category: API
  slug: quantcdn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quantcdn.png
layout: provider
modified: '2026-05-19'
name: QuantCDN
nav: Providers
network: true
overview: 'QuantCDN publishes 38 APIs on the [APIs.io](https://apis.io/) network, including AI Agents API, AI Custom Tools API, AI File Storage API, and 35 more. Tagged areas include CDN, Edge, Static Hosting, Jamstack, and DNS.


  QuantCDN''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Quantcdn Plans Pricing
  plan_count: 3
  slug: quantcdn-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Quantcdn Rate Limits
  slug: quantcdn-rate-limits
score:
  band: thin
  composite: 30.1
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 56.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 38
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quantcdn/refs/heads/main/screenshots/quantcdn-2026-06-20T192409.png
security:
- kind: authentication
  name: Quantcdn Authentication
  slug: quantcdn-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Quantcdn Domain Security
  slug: quantcdn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Quantcdn Vulnerability Disclosure
  slug: quantcdn-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: quantcdn
tags:
- CDN
- Edge
- Static Hosting
- Jamstack
- DNS
- WAF
- Edge Computing
- Key-Value Storage
- AI Inference
website: https://www.quantcdn.io/home
---
