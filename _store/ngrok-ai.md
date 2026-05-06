---
aid: ngrok-ai
name: ngrok AI Gateway
description: ngrok AI Gateway provides traffic management and security for AI APIs including multi-provider routing, automatic failover, LLM prompt inspection, rate limiting, caching, observability, PII redaction, and access control. It enables teams to manage, secure, and monitor traffic to AI model providers (OpenAI, Anthropic, Google, DeepSeek) and self-hosted models such as Ollama and vLLM through an OpenAI-compatible interface.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - AI Gateway
  - API Gateway
  - LLM
  - OpenAI Compatible
  - Routing
  - Security
  - Traffic Management
url: https://raw.githubusercontent.com/api-evangelist/ngrok-ai/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: ngrok-ai:ai-gateway
    name: ngrok AI Gateway
    description: ngrok AI Gateway exposes an OpenAI-compatible HTTP interface for routing requests across multiple AI providers and self-hosted models. Each AI Gateway instance has a unique base URL of the form https://your-ai-gateway.ngrok.app/v1 and accepts standard OpenAI SDK calls including chat completions. Traffic policies provide rate limiting, prompt inspection, PII redaction, response sanitization, model access control, cost-based routing, and automatic provider failover.
    humanURL: https://ngrok.com/docs/ai-gateway/
    baseURL: https://your-ai-gateway.ngrok.app/v1
    tags:
      - AI Gateway
      - API Gateway
      - LLM
      - OpenAI Compatible
      - Routing
      - Security
    properties:
      - type: Documentation
        url: https://ngrok.com/docs/ai-gateway/
      - type: GettingStarted
        url: https://ngrok.com/docs/ai-gateway/quickstart/
      - type: APIReference
        url: https://ngrok.com/docs/ai-gateway/
common:
  - type: Website
    url: https://ngrok.com/ai-gateway
  - type: Documentation
    url: https://ngrok.com/docs/ai-gateway/
  - type: GettingStarted
    url: https://ngrok.com/docs/ai-gateway/quickstart/
  - type: Blog
    url: https://ngrok.com/blog
  - type: Pricing
    url: https://ngrok.com/pricing
  - type: Support
    url: https://ngrok.com/support
  - type: StatusPage
    url: https://status.ngrok.com
  - type: GitHubOrganization
    url: https://github.com/ngrok
  - type: Features
    data:
      - name: Multi-Provider Routing
        description: Direct requests to AI providers including OpenAI, Anthropic, Google, and DeepSeek through a single gateway endpoint.
      - name: Automatic Failover
        description: If one provider or model fails, the gateway automatically tries the next configured model.
      - name: OpenAI SDK Compatibility
        description: Works with official and third-party OpenAI SDKs by changing only the base URL.
      - name: Self-Hosted Model Support
        description: Route requests to local systems such as Ollama or vLLM alongside hosted providers.
      - name: Automatic Model Selection
        description: Use ngrok/auto for intelligent model picking based on configured strategies.
      - name: CEL-Based Selection Strategies
        description: Define custom routing logic using Common Expression Language expressions.
      - name: Cost-Based Routing
        description: Direct traffic to the cheapest available model option meeting requirements.
      - name: Access Control
        description: Restrict which providers and models clients can use by API key, identity, or policy.
      - name: PII Redaction
        description: Inspect and modify content to remove personally identifiable information from prompts and responses.
      - name: Response Sanitization
        description: Modify and filter responses before they reach clients.
      - name: No Provider Account Required
        description: Access OpenAI and Anthropic models without individual provider signup, using ngrok credits.
  - type: UseCases
    data:
      - name: Centralized AI API Management
        description: Manage all AI provider traffic through a single gateway with unified observability and policy enforcement.
      - name: Cost Optimization
        description: Route traffic to the most cost-effective model that meets quality requirements.
      - name: Compliance and Data Protection
        description: Enforce PII redaction and prompt inspection policies before requests leave the organization.
      - name: Multi-Provider Resilience
        description: Failover automatically across providers to maintain AI service availability.
      - name: Local and Hybrid Model Routing
        description: Route between hosted providers and self-hosted models such as Ollama or vLLM.
  - type: Integrations
    data:
      - name: OpenAI
        description: Native OpenAI-compatible interface and routing to OpenAI models.
      - name: Anthropic
        description: Routing and access to Anthropic Claude models through the gateway.
      - name: Google
        description: Routing to Google AI models.
      - name: DeepSeek
        description: Routing to DeepSeek models.
      - name: Ollama
        description: Routing to self-hosted Ollama instances.
      - name: vLLM
        description: Routing to self-hosted vLLM inference servers.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
