---
aid: naftiko
name: Naftiko
description: Naftiko provides spec-driven integration tooling that turns existing data and APIs into governed capabilities for AI. The platform centers on a YAML capability specification, an open-source framework that runs those specs as live MCP, SKILL, and REST services, and Fleet — a governed runtime that makes capabilities discoverable, composable, observable, and cost-bounded.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/naftiko/refs/heads/main/apis.yml
created: '2026-05-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - AI
  - API Integration
  - Capabilities
  - Governance
  - MCP
  - Spec-Driven Integration
apis:
  - aid: naftiko:framework
    name: Naftiko Framework
    description: The Naftiko Framework is an open-source (Apache 2.0) engine for spec-driven integration. It interprets YAML capability specifications and exposes them as live multi-protocol services — including MCP, SKILL, and REST adapters — without requiring Java code. The framework supports OpenAPI 2.0/3.0/3.1 import, format conversion across Protobuf, XML, YAML, CSV, Avro, and JSON, OpenTelemetry tracing, authentication, and inline templating with Mustache and JSONPath.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/naftiko/framework
    tags:
      - Framework
      - MCP
      - Open Source
      - REST
      - SKILL
      - Spec-Driven
    properties:
      - type: Documentation
        url: https://github.com/naftiko/framework/wiki
      - type: GitHubRepository
        url: https://github.com/naftiko/framework
      - type: GettingStarted
        url: https://github.com/naftiko/framework/wiki/Installation
      - type: Tutorials
        url: https://github.com/naftiko/framework/wiki/Tutorial-Part-1
      - type: APIReference
        url: https://github.com/naftiko/framework/wiki/Specification
      - type: ReleaseNotes
        url: https://github.com/naftiko/framework/wiki/Release-Notes
      - type: FAQ
        url: https://github.com/naftiko/framework/wiki/FAQ
  - aid: naftiko:fleet
    name: Naftiko Fleet
    description: Naftiko Fleet is the governed runtime for spec-driven integration. It makes capabilities discoverable through an inventory, composable across domains, observable through telemetry, and cost-bounded through policy controls. Fleet is offered as a Community Edition (freeware) with Standard and Enterprise editions planned, and ships with a VS Code extension and Backstage templates for editing, linting, and cataloguing capabilities.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/naftiko/fleet
    tags:
      - Backstage
      - Fleet
      - Governance
      - IDE
      - Runtime
      - VS Code
    properties:
      - type: Documentation
        url: https://naftiko.io
      - type: GitHubRepository
        url: https://github.com/naftiko/fleet
      - type: IDESupport
        url: https://github.com/naftiko/fleet
      - type: Integrations
        url: https://github.com/naftiko/fleet
  - aid: naftiko:capability-spec
    name: Naftiko Capability Specification
    description: The Naftiko Capability Specification is a YAML-based contract for declaring integration capabilities. Specs are validated by JSON Schema and committed to Git, producing versioned, reviewable artifacts that the framework executes and Fleet governs. The specification covers consume adapters (HTTP, OpenAPI), expose adapters (MCP, SKILL, REST), data transformations, authentication, and domain-driven aggregates.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/naftiko/framework/wiki/Specification
    tags:
      - JSON Schema
      - Specification
      - YAML
    properties:
      - type: APIReference
        url: https://github.com/naftiko/framework/wiki/Specification
      - type: BestPractices
        url: https://github.com/naftiko/framework/wiki/Linting-Guide
      - type: UseCases
        url: https://github.com/naftiko/framework/wiki/Use-Cases
common:
  - type: Documentation
    url: https://naftiko.io
  - type: GitHubOrganization
    url: https://github.com/naftiko
  - type: GettingStarted
    url: https://github.com/naftiko/framework/wiki/Installation
  - type: Blog
    url: https://naftiko.io
  - type: Support
    url: https://github.com/naftiko/framework/discussions
  - type: ReleaseNotes
    url: https://github.com/naftiko/framework/wiki/Release-Notes
  - type: FAQ
    url: https://github.com/naftiko/framework/wiki/FAQ
  - type: Features
    data:
      - name: Spec-Driven Capabilities
        description: Declare integration capabilities entirely in YAML, validated by JSON Schema, with no Java required.
      - name: Multi-Protocol Servers
        description: Expose a single capability simultaneously as MCP, SKILL, and REST endpoints.
      - name: OpenAPI Interoperability
        description: Import Swagger 2.0, OAS 3.0, and OAS 3.1 specifications and export REST adapters as OpenAPI documents.
      - name: Format Conversion
        description: Translate between Protobuf, XML, YAML, CSV, Avro, and JSON inside capability pipelines.
      - name: OpenTelemetry Tracing
        description: Cloud-native observability is built into the framework runtime for every capability invocation.
      - name: Governed Runtime
        description: Fleet adds discovery, composition, observability, and cost controls on top of framework-executed capabilities.
      - name: IDE & Catalog Tooling
        description: VS Code extension for editing and linting capability specs, Backstage templates for scaffolding and cataloguing.
  - type: UseCases
    data:
      - name: AI Agent Integration
        description: Expose enterprise data and APIs to AI agents through governed MCP capabilities instead of bespoke connectors.
      - name: Reuse Across Domains
        description: Convert siloed APIs into a measurable inventory of reusable capabilities that span teams and product lines.
      - name: Policy-Driven Discovery
        description: Apply governance policies at discovery and runtime so AI integrations stay compliant and cost-bounded.
      - name: SaaS and Microservice Sprawl
        description: Tame the integration surface that grows with every new SaaS subscription and internal microservice.
      - name: Right-Sized Context for Agents
        description: Deliver only the context an agent needs into each capability invocation, reducing token cost and risk.
  - type: Integrations
    data:
      - name: Model Context Protocol (MCP)
        description: Capabilities are exposed as MCP servers consumable by Claude, agentic IDEs, and other MCP-aware clients.
      - name: VS Code
        description: Official VS Code extension for editing, linting, and previewing Naftiko capability specs.
      - name: Backstage
        description: Templates and plugins for scaffolding and cataloguing Naftiko capabilities inside Backstage.
      - name: Docker Desktop
        description: Run the framework locally through Docker Desktop integration for development and testing.
      - name: OpenAPI
        description: Import existing OpenAPI documents as consume adapters and export REST adapters back to OpenAPI.
      - name: OpenTelemetry
        description: Emit traces, metrics, and logs from every capability invocation to any OTel-compatible backend.
      - name: Kubernetes
        description: A Kubernetes operator is on the roadmap for running Fleet-governed capabilities as cluster workloads.
  - type: Solutions
    data:
      - name: Naftiko Framework
        description: Open-source Apache 2.0 engine that interprets capability specs and exposes them as MCP, SKILL, and REST services.
      - name: Naftiko Fleet — Community Edition
        description: Freeware governed runtime with discovery, composition, and observability for spec-driven capabilities.
      - name: Naftiko Fleet — Standard and Enterprise
        description: Planned commercial editions of Fleet with expanded governance, policy, and support tiers.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
