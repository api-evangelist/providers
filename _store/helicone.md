---
aid: helicone
url: https://raw.githubusercontent.com/api-evangelist/helicone/refs/heads/main/apis.yml
apis:
- aid: helicone:helicone
  name: Helicone
  tags:
  - AI Gateways
  - Gateways
  - LLM Routing
  humanURL: ' https://www.helicone.ai/'
  properties:
  - url: ' https://www.helicone.ai/'
    type: Documentation
  - url: https://docs.helicone.ai/
    type: Documentation
  - url: https://docs.helicone.ai/getting-started/quick-start
    type: GettingStarted
  - url: https://docs.helicone.ai/getting-started/platform-overview
    type: PlatformOverview
  - url: https://us.helicone.ai/signup
    type: SignUp
  - url: https://us.helicone.ai/signin
    type: Login
  - url: https://us.helicone.ai/dashboard
    type: Portal
  - url: https://us.helicone.ai/developer
    type: DeveloperPortal
  - url: https://www.helicone.ai/pricing
    type: Pricing
  - url: https://docs.helicone.ai/swagger.json
    type: OpenAPI
  - url: https://docs.helicone.ai/rest/request/post-v1requestquery
    type: APIReference
  - url: https://docs.helicone.ai/helicone-headers/header-directory
    type: Headers
  - url: https://github.com/Helicone/helicone
    type: GitHubOrg
  - url: https://www.helicone.ai/blog
    type: Blog
  - url: https://www.helicone.ai/changelog
    type: ChangeLog
  - url: https://status.helicone.ai/
    type: StatusPage
  - url: https://www.helicone.ai/contact
    type: Contact
  - url: https://community.helicone.ai/
    type: Community
  - url: https://discord.gg/2TkeWdXNPQ
    type: Discord
  - url: https://twitter.com/helicone_ai
    type: Twitter
  - url: https://www.linkedin.com/company/helicone/
    type: LinkedIn
  - url: https://www.helicone.ai/privacy
    type: PrivacyPolicy
  - url: https://www.helicone.ai/terms
    type: TermsOfService
  - url: https://docs.helicone.ai/references/data-autonomy
    type: Security
  - url: https://docs.helicone.ai/getting-started/self-host/overview
    type: SelfHosted
  description: Helicone is an open-source LLM observability platform and AI gateway. The worlds fastest-growing AI companies rely on Helicone to route, debug, and analyze their applications. With one line of code, developers can monitor, evaluate, and experiment across 100+ AI models from providers including OpenAI, Anthropic, Google, and more.
- aid: helicone:ai-gateway-api
  name: Helicone AI Gateway API
  tags:
  - AI Gateways
  - AI Models
  - Chat Completions
  - LLM Routing
  humanURL: https://docs.helicone.ai/gateway/overview
  baseURL: https://ai-gateway.helicone.ai
  properties:
  - url: https://docs.helicone.ai/gateway/overview
    type: Documentation
  - url: https://docs.helicone.ai/ai-gateway.openapi.json
    type: OpenAPI
  - url: https://docs.helicone.ai/rest/ai-gateway/post-v1-chat-completions
    type: APIReference
  - url: https://docs.helicone.ai/getting-started/quick-start
    type: GettingStarted
  - url: https://docs.helicone.ai/gateway/provider-routing
    type: ProviderRouting
  - url: https://www.helicone.ai/models
    type: Models
  description: The Helicone AI Gateway API provides OpenAI-compatible endpoints for routing requests to 100+ AI models across providers including OpenAI, Anthropic, Google, Groq, and more. It offers a unified API with automatic provider fallbacks, zero markup pricing, built-in observability, intelligent routing, prompt caching, error handling, and image generation support.
- aid: helicone:request-api
  name: Helicone Request API
  tags:
  - Analytics
  - LLM Observability
  - Requests
  humanURL: https://docs.helicone.ai/rest/request/post-v1requestquery
  baseURL: https://api.helicone.ai
  properties:
  - url: https://docs.helicone.ai/rest/request/post-v1requestquery
    type: Documentation
  - url: https://docs.helicone.ai/swagger.json
    type: OpenAPI
  description: The Helicone Request API allows developers to query, retrieve, and manage LLM request data. Endpoints include querying requests with filters, retrieving requests by IDs, submitting feedback and scores, uploading request assets, and updating request properties.
- aid: helicone:prompt-api
  name: Helicone Prompt API
  tags:
  - Prompt Management
  - Prompts
  - Versioning
  humanURL: https://docs.helicone.ai/rest/prompts/post-v1prompt-2025
  baseURL: https://api.helicone.ai
  properties:
  - url: https://docs.helicone.ai/rest/prompts/post-v1prompt-2025
    type: Documentation
  - url: https://docs.helicone.ai/features/advanced-usage/prompts/overview
    type: Overview
  - url: https://docs.helicone.ai/swagger.json
    type: OpenAPI
  description: The Helicone Prompt API provides endpoints for creating, querying, updating, and deleting prompts and prompt versions. It supports prompt environments, tagging, versioning, and production deployment workflows for managing prompts across the development lifecycle.
- aid: helicone:experiment-api
  name: Helicone Experiment API
  tags:
  - Datasets
  - Evaluations
  - Experiments
  humanURL: https://docs.helicone.ai/features/experiments
  baseURL: https://api.helicone.ai
  properties:
  - url: https://docs.helicone.ai/features/experiments
    type: Documentation
  - url: https://docs.helicone.ai/rest/experiment/post-v1experiment-evaluatorsrun
    type: APIReference
  - url: https://docs.helicone.ai/swagger.json
    type: OpenAPI
  description: The Helicone Experiment API enables developers to create experiment datasets, run evaluators, update experiment metadata, and manage experiment workflows. It supports systematic prompt experimentation and evaluation to optimize AI application performance.
- aid: helicone:evals-api
  name: Helicone Evals API
  tags:
  - Evaluations
  - LLM Quality
  - Scoring
  humanURL: https://docs.helicone.ai/rest/evals/post-v1evals
  baseURL: https://api.helicone.ai
  properties:
  - url: https://docs.helicone.ai/rest/evals/post-v1evals
    type: Documentation
  - url: https://docs.helicone.ai/features/advanced-usage/scores
    type: Overview
  - url: https://docs.helicone.ai/swagger.json
    type: OpenAPI
  description: The Helicone Evals API provides endpoints for creating evaluations, querying evaluation results, retrieving scores, and analyzing score distributions. It enables developers to systematically assess and monitor the quality of their AI model outputs.
- aid: helicone:session-api
  name: Helicone Session API
  tags:
  - Debugging
  - Sessions
  - Tracing
  humanURL: https://docs.helicone.ai/features/sessions
  baseURL: https://api.helicone.ai
  properties:
  - url: https://docs.helicone.ai/features/sessions
    type: Documentation
  - url: https://docs.helicone.ai/rest/session/post-v1sessionquery
    type: APIReference
  - url: https://docs.helicone.ai/swagger.json
    type: OpenAPI
  description: The Helicone Session API allows developers to query sessions, retrieve session metrics, and submit session feedback. Sessions enable tracing and debugging of multi-step LLM interactions and agent workflows in real time.
- aid: helicone:user-api
  name: Helicone User API
  tags:
  - Analytics
  - Metrics
  - Users
  humanURL: https://docs.helicone.ai/features/advanced-usage/user-metrics
  baseURL: https://api.helicone.ai
  properties:
  - url: https://docs.helicone.ai/features/advanced-usage/user-metrics
    type: Documentation
  - url: https://docs.helicone.ai/rest/user/post-v1userquery
    type: APIReference
  - url: https://docs.helicone.ai/swagger.json
    type: OpenAPI
  description: The Helicone User API provides endpoints for querying user data, retrieving user metrics, and getting user metrics overviews. It enables developers to track per-user usage, costs, and performance analytics across their AI applications.
- aid: helicone:webhook-api
  name: Helicone Webhook API
  tags:
  - Events
  - Notifications
  - Webhooks
  humanURL: https://docs.helicone.ai/features/webhooks
  baseURL: https://api.helicone.ai
  properties:
  - url: https://docs.helicone.ai/features/webhooks
    type: Documentation
  - url: https://docs.helicone.ai/rest/webhooks/get-v1webhooks
    type: APIReference
  - url: https://docs.helicone.ai/swagger.json
    type: OpenAPI
  description: The Helicone Webhook API provides endpoints for creating, listing, and deleting webhooks. Webhooks enable developers to receive real-time notifications about events in their Helicone workspace, supporting integration with external systems and automated workflows.
- aid: helicone:model-registry-api
  name: Helicone Model Registry API
  tags:
  - AI Models
  - Models
  - Registry
  humanURL: https://docs.helicone.ai/rest/models/get-v1public-model-registry-models
  baseURL: https://api.helicone.ai
  properties:
  - url: https://docs.helicone.ai/rest/models/get-v1public-model-registry-models
    type: Documentation
  - url: https://docs.helicone.ai/swagger.json
    type: OpenAPI
  description: The Helicone Model Registry API provides a public endpoint for retrieving the complete catalog of AI models and provider endpoints that the Helicone AI Gateway can route to. This allows developers to discover available models and their capabilities.
- aid: helicone:trace-api
  name: Helicone Trace API
  tags:
  - Logging
  - Observability
  - Tracing
  humanURL: https://docs.helicone.ai/rest/trace/post-v1tracelog
  baseURL: https://api.helicone.ai
  properties:
  - url: https://docs.helicone.ai/rest/trace/post-v1tracelog
    type: Documentation
  - url: https://docs.helicone.ai/swagger.json
    type: OpenAPI
  description: The Helicone Trace API provides endpoints for logging traces from AI applications. It enables developers to capture and log multi-step interactions, tool calls, and agent workflows for observability and debugging purposes.
- aid: helicone:dashboard-api
  name: Helicone Dashboard API
  tags:
  - Analytics
  - Dashboard
  - Scoring
  humanURL: https://docs.helicone.ai/rest/dashboard/post-v1dashboardscoresquery
  baseURL: https://api.helicone.ai
  properties:
  - url: https://docs.helicone.ai/rest/dashboard/post-v1dashboardscoresquery
    type: Documentation
  - url: https://docs.helicone.ai/swagger.json
    type: OpenAPI
  description: The Helicone Dashboard API provides endpoints for querying dashboard scores and analytics data. It supports programmatic access to the aggregated metrics and scoring data available in the Helicone dashboard interface.
- aid: helicone:property-api
  name: Helicone Property API
  tags:
  - Custom Properties
  - Metadata
  - Properties
  humanURL: https://docs.helicone.ai/features/advanced-usage/custom-properties
  baseURL: https://api.helicone.ai
  properties:
  - url: https://docs.helicone.ai/features/advanced-usage/custom-properties
    type: Documentation
  - url: https://docs.helicone.ai/rest/property/post-v1propertyquery
    type: APIReference
  - url: https://docs.helicone.ai/swagger.json
    type: OpenAPI
  description: The Helicone Property API provides endpoints for querying custom properties attached to requests. Custom properties allow developers to segment and filter their LLM request data by arbitrary metadata such as environment, feature, user cohort, or any other dimension.
name: Helicone
tags:
- AI Gateways
- AI Monitoring
- Gateways
- LLM Observability
- LLM Routing
- Prompt Management
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-02'
modified: '2026-04-07'
position: Consumer
description: Helicone is an open-source LLM observability platform and AI gateway that helps developers monitor, evaluate, and experiment with their AI applications. The worlds fastest-growing AI companies rely on Helicone to route, debug, and analyze their applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

