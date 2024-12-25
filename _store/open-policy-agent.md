---
specificationVersion: '0.19'

aid: open-policy-agent

name: Open Policy Agent

tags:

  - Policies

  - Standards

type: Index

image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg

access: 3rd-Party

created: '2024-11-18'

modified: '2024-11-18'

position: Consumer

description: >-

  Stop using a different policy language, policy model, and policy API for every

  product and service you use. Use OPA for a unified toolset and framework for

  policy across the cloud native stack. Whether for one service or for all your

  services, use OPA to decouple policy from the service's code so you can

  release, analyze, and review policies (which security and compliance teams

  love) without sacrificing availability or performance.

maintainers:

  - FN: Kin Lane

    email: info@apievangelist.com

url: >-

  https://raw.githubusercontent.com/api-search/open-policy-agent/refs/heads/main/apis.yml

apis:

  - aid: open-policy-agent:policy-api

    name: Policy API

    tags:

      - Policies

    humanURL: https://www.openpolicyagent.org/docs/latest/rest-api/#policy-api

    properties:

      - url: https://www.openpolicyagent.org/docs/latest/rest-api/#policy-api

        type: Documentation

      - url: openapi/policy-api.yml

        type: OpenAPI

      - url: policy/bruno.json

        type: BrunoCollection

      - url: >-

          https://api-evangelist.postman.co/workspace/Open-Policy-Agentbcc99d6c-728a-4d86-83fd-b6495f5e8fb8/collection/35240-19ce2c88-97b8-4f58-a101-b8be70794a85

        type: PostmanCollection

    description: API for managing policy modules, allowing CRUD operations.

  - aid: open-policy-agent:data-api

    name: Data API

    tags:

      - Data

      - Documents

    humanURL: https://www.openpolicyagent.org/docs/latest/rest-api/#data-api

    properties:

      - url: https://www.openpolicyagent.org/docs/latest/rest-api/#data-api

        type: Documentation

      - url: openapi/data-api.yml

        type: OpenAPI

      - url: data/bruno.json

        type: BrunoCollection

      - url: >-

          https://api-evangelist.postman.co/workspace/Open-Policy-Agentbcc99d6c-728a-4d86-83fd-b6495f5e8fb8/collection/35240-96c58dc4-3514-48ee-a35f-a9c2aeb14fa0

        type: PostmanCollection

    description: API for reading and writing documents in OPA (Open Policy Agent).

  - aid: open-policy-agent:query-api

    name: Query API

    tags:

      - Queries

    humanURL: https://www.openpolicyagent.org/docs/latest/rest-api/#query-api

    properties:

      - url: https://www.openpolicyagent.org/docs/latest/rest-api/#query-api

        type: Documentation

      - url: openapi/query-api.yml

        type: OpenAPI

      - url: query/bruno.json

        type: BrunoCollection

      - url: >-

          https://api-evangelist.postman.co/workspace/Open-Policy-Agentbcc99d6c-728a-4d86-83fd-b6495f5e8fb8/collection/35240-9170dd84-c3d5-45a4-9efc-9ef6ab30744e

        type: PostmanCollection

    description: API for executing simple and ad-hoc queries in OPA (Open Policy Agent).

  - aid: open-policy-agent:compile-api

    name: Compile API

    tags:

      - Compile

      - Evaluation

    humanURL: https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api

    properties:

      - url: https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api

        type: Documentation

      - url: openapi/compile-api.yml

        type: OpenAPI

      - url: compile/bruno.json

        type: BrunoCollection

      - url: >-

          https://api-evangelist.postman.co/workspace/Open-Policy-Agentbcc99d6c-728a-4d86-83fd-b6495f5e8fb8/collection/35240-1e1d8e0e-7157-4b7f-99cf-611fa56a0c3c

        type: PostmanCollection

    description: API for partially evaluating Rego queries in OPA (Open Policy Agent).

  - aid: open-policy-agent:health-api

    name: Health API

    tags:

      - Health

      - Availability

    humanURL: https://www.openpolicyagent.org/docs/latest/rest-api/#health-api

    properties:

      - url: https://www.openpolicyagent.org/docs/latest/rest-api/#health-api

        type: Documentation

      - url: openapi/health-api.yml

        type: OpenAPI

      - url: health/bruno.json

        type: BrunoCollection

      - url: >-

          https://api-evangelist.postman.co/workspace/Open-Policy-Agentbcc99d6c-728a-4d86-83fd-b6495f5e8fb8/collection/35240-198cdb4f-e1d1-44c4-aa1f-ef8f66760d1a

        type: PostmanCollection

    description: >-

      API for checking the health and readiness of an OPA (Open Policy Agent)

      server.

  - aid: open-policy-agent:config-api

    name: Config API

    tags:

      - Configurations

    humanURL: https://www.openpolicyagent.org/docs/latest/rest-api/#config-api

    properties:

      - url: https://www.openpolicyagent.org/docs/latest/rest-api/#config-api

        type: Documentation

      - url: openapi/config-api.yml

        type: OpenAPI

      - url: config/bruno.json

        type: BrunoCollection

      - url: >-

          https://api-evangelist.postman.co/workspace/Open-Policy-Agentbcc99d6c-728a-4d86-83fd-b6495f5e8fb8/collection/35240-979cbaf7-8515-4fd2-8035-134685590967

        type: PostmanCollection

    description: >-

      API for retrieving OPA's active configuration, including discovered

      configurations.

  - aid: open-policy-agent:status-api

    name: Status API

    tags:

      - Status

    humanURL: https://www.openpolicyagent.org/docs/latest/rest-api/#status-api

    properties:

      - url: https://www.openpolicyagent.org/docs/latest/rest-api/#status-api

        type: Documentation

      - url: openapi/status-api.yml

        type: OpenAPI

      - url: status/bruno.json

        type: BrunoCollection

      - url: >-

          https://api-evangelist.postman.co/workspace/Open-Policy-Agentbcc99d6c-728a-4d86-83fd-b6495f5e8fb8/collection/35240-b4943ca3-d651-4c68-a003-e6ca7feace03

        type: PostmanCollection

    description: >-

      API for accessing OPA (Open Policy Agent) status information via a

      pull-based mechanism.

common:

  - name: Documentation

    url: https://www.openpolicyagent.org/docs/latest/rest-api/

    type: Documentation

  - name: Authentication

    url: https://www.openpolicyagent.org/docs/latest/rest-api/#authentication

    type: Authentication

  - name: Errors

    url: https://www.openpolicyagent.org/docs/latest/rest-api/#errors

    type: Errors

  - name: Postman Workspace

    url: https://www.postman.com/api-evangelist/open-policy-agent/overview

    type: PostmanWorkspace

  - name: GitHub Repository

    url: https://github.com/api-search/open-policy-agent

    type: GitHubRepository

---