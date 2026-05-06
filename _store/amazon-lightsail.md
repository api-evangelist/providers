---
name: Amazon Lightsail
description: Amazon Lightsail is a virtual private server (VPS) provider and is the easiest way to get started with AWS for developers, small businesses, students, and other users who need a solution to build and host their applications on cloud. Lightsail provides developers compute, storage, and networking capacity and capabilities to deploy and manage websites and web applications in the cloud.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://apis.io/amazon-lightsail
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon Lightsail API
    description: The Amazon Lightsail API provides programmatic access to manage Lightsail resources including instances, containers, databases, disks, load balancers, certificates, distributions, and DNS zones.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    baseURL: https://lightsail.amazonaws.com
    properties:
      - type: documentation
        url: https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html
      - type: openapi
        url: openapi/openapi.yml
      - type: openapi
        url: https://api.apis.guru/v2/specs/amazonaws.com/lightsail/latest/openapi.yaml
      - type: json-schema
        url: json-schema/json-schema.yml
      - type: json-ld
        url: json-ld/json-ld.yml
      - type: pricing
        url: https://aws.amazon.com/lightsail/pricing/
      - type: getting-started
        url: https://aws.amazon.com/lightsail/getting-started/
      - type: faq
        url: https://aws.amazon.com/lightsail/faq/
      - type: JSONSchema
        url: json-schema/amazon-lightsail-instance-schema.json
      - type: JSONLD
        url: json-ld/amazon-lightsail-context.jsonld
common:
  - type: portal
    url: https://aws.amazon.com/
  - type: website
    url: https://aws.amazon.com/lightsail/
  - type: documentation
    url: https://docs.aws.amazon.com/lightsail/
  - type: terms-of-service
    url: https://aws.amazon.com/service-terms/
  - type: privacy-policy
    url: https://aws.amazon.com/privacy/
  - type: support
    url: https://aws.amazon.com/premiumsupport/
  - type: blog
    url: https://aws.amazon.com/blogs/compute/
  - type: github
    url: https://github.com/aws
  - type: console
    url: https://lightsail.aws.amazon.com/
  - type: sign-up
    url: https://portal.aws.amazon.com/billing/signup
  - type: login
    url: https://signin.aws.amazon.com/
  - type: status
    url: https://health.aws.amazon.com/health/status
  - type: knowledge-center
    url: https://repost.aws/knowledge-center
  - type: youtube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: stack-overflow
    url: https://stackoverflow.com/questions/tagged/amazon-lightsail
  - type: contact
    url: https://aws.amazon.com/contact-us/
  - type: security
    url: https://aws.amazon.com/security/
  - type: compliance
    url: https://aws.amazon.com/compliance/
  - type: Features
    data:
      - name: Simple Virtual Servers
        description: Launch virtual servers with pre-configured Linux/Windows environments in minutes.
      - name: Managed Databases
        description: Deploy managed databases (MySQL, PostgreSQL) without server management.
      - name: Containers
        description: Deploy containerized applications using Lightsail container services.
      - name: CDN Distributions
        description: Create CloudFront-powered CDN distributions for faster content delivery.
      - name: Predictable Pricing
        description: Fixed monthly pricing with no surprise bills including compute, storage, and data transfer.
  - type: UseCases
    data:
      - name: WordPress Hosting
        description: Host WordPress sites with pre-configured LAMP stacks at low, predictable cost.
      - name: Web Application Development
        description: Develop and test web applications on simple cloud infrastructure.
      - name: Small Business Websites
        description: Power small business websites with affordable, managed cloud hosting.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Connect Lightsail instances to S3 buckets for object storage.
      - name: AWS CloudFront
        description: Distribute Lightsail content globally via CloudFront CDN distributions.
      - name: Amazon Route 53
        description: Manage DNS for Lightsail resources using Route 53.
      - name: Amazon EC2
        description: Migrate Lightsail instances to EC2 when you need more control.
  - type: SpectralRules
    url: rules/amazon-lightsail-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-lightsail-workflow.yaml
  - type: Vocabulary
    url: vocabulary/amazon-lightsail-vocabulary.yaml
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
---
