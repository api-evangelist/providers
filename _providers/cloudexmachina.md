---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-17'
  detail: Cloud ex Machina is a real software company that ships a per-tenant SaaS product (Dex) and genuinely maintains public Docusaurus documentation, but it operates no developer program at all — no API reference among the 23 pages in its docs sitemap, no api.cloudexmachina.io host in DNS, no MCP server, no agent card, and no client SDK in any language registry; its only developer-facing distributables are AWS onboarding IaC (a Terraform Registry module at v0.6.0, a CloudFormation template, and a GitHub Action).
  evidence:
  - status: 200
    url: https://docs.cloudexmachina.io/sitemap.xml
  - status: 0
    url: https://api.cloudexmachina.io/openapi.json
  - status: 200
    url: https://app.cloudexmachina.io/openapi.json
  - status: 404
    url: https://www.cloudexmachina.io/.well-known/agent-card.json
  - status: 200
    url: https://registry.terraform.io/v1/modules/cxmlabs/cxm-integration/aws
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: Cloud ex Machina (CxM) builds Dex, an agentic AI teammate for cloud cost and governance management. Dex continuously maps AWS, Azure, GCP and Kubernetes estates read-only and agentless, infers resource ownership by keeping the cloud connected to the organization's people and code, investigates cost and governance findings, and delivers review-ready remediation — pull requests, scripts and CLI instructions — to the engineers who can act, inside the tools they already use. The platform integrates with GitHub, GitLab, Jira, Linear, Notion, ServiceNow, Slack and Microsoft Teams, ingests non-cloud AI spend from Anthropic, and runs as a per-tenant SaaS with SAML 2.0 SSO. Cloud ex Machina publishes no public REST API or machine-readable specification; its developer-facing surface is cloud onboarding distributed as a Terraform Registry module, a CloudFormation template and a GitHub Action.
image: https://www.cloudexmachina.io/hubfs/cxm_logo.svg
layout: provider
modified: '2026-08-17'
name: Cloud Ex Machina
nav: Providers
network: true
random_paper: 136
slug: cloudexmachina
tags:
- Company
- Infrastructure
- Cloud
- FinOps
- Cloud Cost Optimization
- Cloud Governance
- AI Agents
- Cloud Management
- Terraform
- Kubernetes
---
