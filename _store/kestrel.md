---
aid: kestrel
url: https://raw.githubusercontent.com/api-evangelist/kestrel/refs/heads/main/apis.yml
apis:
- aid: kestrel:platform
  name: Kestrel Platform
  tags:
  - AI Agents
  - Cloud Security
  - Incident Response
  - Kubernetes
  humanURL: https://docs.usekestrel.ai/
  properties:
  - url: https://docs.usekestrel.ai/
    type: Documentation
  - url: https://docs.usekestrel.ai/quickstart
    type: GettingStarted
  - url: https://platform.usekestrel.ai/register
    type: SignUp
  description: Kestrel AI provides an AI-native cloud incident response platform that uses autonomous agents to detect, investigate, and remediate Kubernetes and cloud infrastructure incidents. The platform monitors clusters continuously, identifies root causes, and generates production-ready fixes delivered as pull requests via GitOps workflows. It integrates with major cloud providers, observability tools, and CI/CD platforms to provide end-to-end incident management.
- aid: kestrel:kubernetes-operator
  name: Kestrel Kubernetes Operator
  tags:
  - gRPC
  - Helm
  - Kubernetes
  - Operators
  humanURL: https://docs.usekestrel.ai/kubernetes/configuration
  properties:
  - url: https://docs.usekestrel.ai/kubernetes/configuration
    type: Documentation
  - url: https://github.com/KestrelAI/Kestrel-Operator
    type: GitHubOrganization
  description: The Kestrel Kubernetes Operator is an open-source Go-based operator that connects Kubernetes clusters to the Kestrel AI platform. It communicates via bidirectional gRPC streaming over mTLS with OAuth2 authentication, streaming resource metadata, logs, events, and network telemetry. The operator supports OpenTelemetry OTLP ingestion and Istio Access Log Service integration for comprehensive observability. It is deployed via Helm chart from the GitHub Container Registry.
name: Kestrel
tags:
- AI Agents
- Cloud Security
- Incident Response
- Kubernetes
- Observability
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Kestrel AI is a YC-backed startup building an AI-native cloud incident response platform. Founded by former Illumio Kubernetes Security engineers, Kestrel uses autonomous AI agents to detect, investigate, and remediate infrastructure incidents across Kubernetes and cloud environments. The platform provides continuous monitoring, root cause analysis, and automated remediation through GitOps workflows, integrating with Slack, PagerDuty, GitHub, GitLab, AWS, and major observability platforms.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

