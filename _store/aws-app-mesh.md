---
aid: aws-app-mesh
name: AWS App Mesh
description: 'AWS App Mesh is a service mesh based on the Envoy proxy that provides application-level networking to make it easy for services to communicate with each other across multiple types of compute infrastructure including Amazon ECS, EKS, EC2, and Fargate. App Mesh standardizes service communication, giving end-to-end visibility and helping ensure high availability. Note: AWS App Mesh is deprecated; Amazon ECS Service Connect is the recommended replacement for new workloads.'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Deprecated
  - Envoy
  - Microservices
  - Networking
  - Service Mesh
url: https://raw.githubusercontent.com/api-evangelist/aws-app-mesh/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: aws-app-mesh:aws-app-mesh-api
    name: AWS App Mesh API
    description: API for creating and managing App Mesh service meshes, virtual services, virtual nodes, virtual routers, routes, and gateway routes. The service is based on Envoy proxy and provides service discovery, traffic routing, and observability for microservices.
    humanURL: https://aws.amazon.com/app-mesh/
    baseURL: https://appmesh.amazonaws.com
    tags:
      - Deprecated
      - Envoy
      - Microservices
      - Networking
      - Service Mesh
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/aws-app-mesh-openapi.yaml
      - type: APIReference
        url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/Welcome.html
      - type: Authentication
        url: https://docs.aws.amazon.com/app-mesh/latest/userguide/security-iam.html
      - type: Quickstart
        url: https://docs.aws.amazon.com/app-mesh/latest/userguide/getting-started-ecs.html
      - type: Documentation
        url: https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect/
        title: Migration Guide to ECS Service Connect
common:
  - type: Website
    url: https://aws.amazon.com/app-mesh/
  - type: Documentation
    url: https://docs.aws.amazon.com/app-mesh/
  - type: GettingStarted
    url: https://docs.aws.amazon.com/app-mesh/latest/userguide/getting_started.html
  - type: Pricing
    url: https://aws.amazon.com/app-mesh/pricing/
  - type: FAQ
    url: https://aws.amazon.com/app-mesh/faqs/
  - type: Authentication
    url: https://docs.aws.amazon.com/app-mesh/latest/userguide/security-iam.html
  - type: Console
    url: https://console.aws.amazon.com/appmesh/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: SpectralRules
    url: rules/aws-app-mesh-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/aws-app-mesh-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/service-mesh-workflow.yaml
  - type: Features
    data:
      - name: Service Mesh Management
        description: Create and manage service meshes spanning Amazon ECS, EKS, EC2, and Fargate compute environments.
      - name: Virtual Node Configuration
        description: Define virtual nodes representing actual services with listener ports, health checks, and service discovery backends.
      - name: Traffic Routing
        description: Configure virtual routers and routes for weighted routing, retry policies, and timeout configurations.
      - name: Envoy Proxy Integration
        description: Automatically injects and manages Envoy sidecar proxies for transparent service-to-service communication.
      - name: Observability
        description: Export metrics, logs, and traces from Envoy proxies to AWS CloudWatch, X-Ray, and third-party tools.
      - name: mTLS Encryption
        description: Enable mutual TLS encryption between services within the mesh for zero-trust networking.
      - name: Virtual Gateways
        description: Configure ingress traffic from outside the mesh to virtual services using gateway routes.
      - name: Multi-Account Mesh Sharing
        description: Share service meshes across AWS accounts using AWS Resource Access Manager.
  - type: UseCases
    data:
      - name: Microservices Communication
        description: Standardize and control service-to-service networking for containerized microservices applications.
      - name: Traffic Management
        description: Implement canary deployments, A/B testing, and weighted routing without application code changes.
      - name: Observability and Debugging
        description: Capture end-to-end metrics and traces to identify performance bottlenecks and service failures.
      - name: Zero-Trust Networking
        description: Enforce mTLS encryption between services for internal network security compliance.
  - type: Integrations
    data:
      - name: Amazon ECS
        description: Automatically inject Envoy sidecars into ECS task definitions.
      - name: Amazon EKS
        description: Integrate with Kubernetes pod networking using the App Mesh controller for Kubernetes.
      - name: AWS X-Ray
        description: Export distributed traces from Envoy proxies to X-Ray for performance analysis.
      - name: Amazon CloudWatch
        description: Send Envoy proxy metrics to CloudWatch for monitoring and alerting.
      - name: AWS Cloud Map
        description: Use Cloud Map for service discovery within the mesh.
      - name: Amazon EC2
        description: Run Envoy sidecar proxies alongside EC2-hosted services.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
