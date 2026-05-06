---
aid: configuration-language
url: https://raw.githubusercontent.com/api-evangelist/configuration-language/refs/heads/main/apis.yml
name: Configuration Language
x-type: topic
description: Configuration languages are formats and DSLs used to express the desired state of software systems, infrastructure, applications, and APIs. Configuration languages span a spectrum from simple text-based formats (INI, JSON, YAML, TOML) to typed and templated formats (HCL, Cue, Dhall, Pkl, Jsonnet, KDL) that support imports, schemas, and validation. The choice of configuration language shapes how teams describe Kubernetes manifests, Terraform infrastructure, OpenAPI specs, CI pipelines, and developer environments.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Configuration
  - DSL
  - Infrastructure as Code
  - Schemas
  - Serialization
  - Templating
  - YAML
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: configuration-language:yaml
    name: YAML
    description: YAML Ain't Markup Language is a human-friendly data serialization language. YAML 1.2 is widely used for configuration in Kubernetes, OpenAPI, GitHub Actions, Ansible, and many other ecosystems. YAML supports comments, scalars, sequences, mappings, anchors, and tags.
    humanURL: https://yaml.org/
    baseURL: https://yaml.org
    tags:
      - Human Readable
      - Serialization
      - Standards
      - YAML
    properties:
      - type: Specification
        url: https://yaml.org/spec/1.2.2/
      - type: Documentation
        url: https://yaml.org/
      - type: Reference
        url: https://github.com/yaml/yaml-spec
    x-features:
      - Indentation-based syntax with comments
      - Anchors and aliases for reuse
      - Schemas (failsafe, JSON, core)
      - Used by Kubernetes, OpenAPI, Ansible, GitHub Actions
  - aid: configuration-language:json
    name: JSON
    description: JavaScript Object Notation is a lightweight data interchange format defined by RFC 8259 and ECMA-404. JSON is heavily used as a configuration format in Node.js (package.json), VS Code settings, and many other tools, and is the foundation for JSON Schema-based validation.
    humanURL: https://www.json.org/
    baseURL: https://www.json.org
    tags:
      - ECMA
      - IETF
      - Interchange
      - JSON
    properties:
      - type: Specification
        url: https://www.rfc-editor.org/rfc/rfc8259
      - type: Specification
        url: https://www.ecma-international.org/publications-and-standards/standards/ecma-404/
      - type: Reference
        url: https://json-schema.org/
    x-features:
      - Strict, simple, well-supported across languages
      - JSON Schema for validation
      - No native comments (mitigated by JSON5, JSONC)
  - aid: configuration-language:toml
    name: TOML
    description: Tom's Obvious, Minimal Language is a config file format designed to be human-readable and unambiguous. TOML is used by Cargo for Rust projects, Python packaging via pyproject.toml, and Hugo site config.
    humanURL: https://toml.io/
    baseURL: https://toml.io
    tags:
      - Configuration
      - Human Readable
      - TOML
    properties:
      - type: Specification
        url: https://toml.io/en/v1.0.0
      - type: GitHubRepository
        url: https://github.com/toml-lang/toml
    x-features:
      - Strong typing with dates, integers, floats, booleans, arrays
      - Tables and inline tables
      - Used by Cargo (Rust) and pyproject.toml (Python)
  - aid: configuration-language:hcl
    name: HCL
    description: HashiCorp Configuration Language is a structured configuration language designed for human authoring of complex configurations. HCL underpins Terraform, Packer, Vault, Consul, and Nomad and supports expressions, variables, functions, and blocks.
    humanURL: https://github.com/hashicorp/hcl
    baseURL: https://github.com
    tags:
      - HCL
      - HashiCorp
      - Infrastructure as Code
      - Terraform
    properties:
      - type: GitHubRepository
        url: https://github.com/hashicorp/hcl
      - type: Documentation
        url: https://developer.hashicorp.com/terraform/language
    x-features:
      - Block-and-attribute syntax with native expressions
      - JSON-equivalent representation
      - Variables, locals, and functions
      - Foundation of Terraform infrastructure code
  - aid: configuration-language:cue
    name: Cue
    description: Cue is an open source data validation language with a powerful type system and unification semantics. Cue is used to validate, generate, and transform configuration for Kubernetes, OpenAPI, and Terraform.
    humanURL: https://cuelang.org/
    baseURL: https://cuelang.org
    tags:
      - Cue
      - Schema
      - Type System
      - Validation
    properties:
      - type: Documentation
        url: https://cuelang.org/docs/
      - type: GitHubRepository
        url: https://github.com/cue-lang/cue
    x-features:
      - Types and values are unified
      - First-class schemas with constraints
      - Importable, composable definitions
      - Code generation and validation tooling
  - aid: configuration-language:dhall
    name: Dhall
    description: Dhall is a programmable configuration language that adds types and functions to JSON and YAML. Dhall expressions are total (always terminate) and remote imports are content-addressed for safety.
    humanURL: https://dhall-lang.org/
    baseURL: https://dhall-lang.org
    tags:
      - Dhall
      - Functional
      - Total
      - Type Safe
    properties:
      - type: Documentation
        url: https://dhall-lang.org/
      - type: GitHubRepository
        url: https://github.com/dhall-lang/dhall-lang
    x-features:
      - Total, statically typed expressions
      - Pure functions, types, and imports
      - Renderable to JSON, YAML, plain Dhall
  - aid: configuration-language:pkl
    name: Pkl
    description: Pkl is Apple's open source configuration language with a focus on type safety, composition, and runtime templating. Pkl can render to YAML, JSON, plist, and other formats and offers IDE tooling and language bindings.
    humanURL: https://pkl-lang.org/
    baseURL: https://pkl-lang.org
    tags:
      - Apple
      - Pkl
      - Templating
      - Type Safe
    properties:
      - type: Documentation
        url: https://pkl-lang.org/main/current/
      - type: GitHubRepository
        url: https://github.com/apple/pkl
    x-features:
      - First-class types, classes, and modules
      - Renders to YAML, JSON, plist, properties, and Pcf
      - Integrations for Java, Kotlin, Swift, Go
  - aid: configuration-language:jsonnet
    name: Jsonnet
    description: Jsonnet is a data templating language designed for elegant generation of JSON and YAML. It is used heavily for Kubernetes manifests, Grafana dashboards (Grafonnet), and Bazel-based tooling.
    humanURL: https://jsonnet.org/
    baseURL: https://jsonnet.org
    tags:
      - Generation
      - Jsonnet
      - Templating
    properties:
      - type: Documentation
        url: https://jsonnet.org/learning/tutorial.html
      - type: GitHubRepository
        url: https://github.com/google/jsonnet
    x-features:
      - JSON-superset templating language
      - Functions, mixins, and inheritance
      - Used by Grafana dashboards (Grafonnet) and Tanka
  - aid: configuration-language:kdl
    name: KDL
    description: KDL is a node-oriented document language combining the readability of YAML and TOML with a unique tree-shaped grammar. KDL is used by Zellij, Helix, and other tools.
    humanURL: https://kdl.dev/
    baseURL: https://kdl.dev
    tags:
      - KDL
      - Tree
    properties:
      - type: Specification
        url: https://github.com/kdl-org/kdl/blob/main/SPEC.md
      - type: Documentation
        url: https://kdl.dev/
    x-features:
      - Node-and-property document model
      - Distinct query language KQL for navigation
      - Schema language KDL Schema
common:
  - type: Reference
    url: https://en.wikipedia.org/wiki/Configuration_file
  - type: Reference
    url: https://docs.kernel.org/admin-guide/configuration.html
  - type: Resources
    url: https://github.com/avelino/awesome-go#configuration
  - type: Reference
    url: https://json-schema.org/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
