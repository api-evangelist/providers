---
aid: amazon-efs
url: https://raw.githubusercontent.com/api-evangelist/amazon-efs/refs/heads/main/apis.yml
apis:
- name: Amazon EFS API
  description: API for managing Amazon EFS file systems, mount targets, and related resources.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  url: https://aws.amazon.com/efs/
  baseURL: https://elasticfilesystem.amazonaws.com
  properties:
  - type: documentation
    url: https://docs.aws.amazon.com/efs/latest/ug/
  - type: openapi
    url: openapi/amazon-efs-openapi.yml
  - type: openapi
    url: https://api.apis.guru/v2/specs/amazonaws.com/elasticfilesystem/2015-02-01/openapi.yaml
  - type: json-schema
    url: json-schema/amazon-efs-filesystem-schema.json
  - type: json-ld
    url: json-ld/amazon-efs-context.jsonld
  - type: pricing
    url: https://aws.amazon.com/efs/pricing/
  - type: getting-started
    url: https://aws.amazon.com/efs/getting-started/
  - type: faq
    url: https://aws.amazon.com/efs/faqs/
  - type: user-guide
    url: https://docs.aws.amazon.com/efs/latest/ug/
  - type: api-reference
    url: https://docs.aws.amazon.com/efs/latest/ug/API_Reference.html
  - type: cli-reference
    url: https://docs.aws.amazon.com/cli/latest/reference/efs/
  - type: security
    url: https://docs.aws.amazon.com/efs/latest/ug/security.html
name: Amazon EFS
tags:
- Amazon Web Services
- AWS
- EFS
- Elastic File System
- File Storage
- NFS
- Serverless
- Storage
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Elastic File System (EFS) provides a simple, serverless, set-and-forget elastic file system for use with AWS cloud services and on-premises resources. EFS is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

