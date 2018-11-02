# Ansible Kong Module

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

An Ansible module to configure the [Kong](http://getkong.com) API gateway.

Based on the changes from [Klarrio/ansible-kong-module](https://github.com/Klarrio/ansible-kong-module), which were based
on the original work of Cristo Crampton.

For an introduction to Kong + Ansible, take a look at [Kong Up and Running](http://blog.toast38coza.me/kong-up-and-running).


# Description

This package aims to provide a stable, idempotent Ansible module for the Kong API gateway.

Support for Kong versions < 0.12 was dropped off.

## Key difference from Klarrio fork

* support only for the new Kong API (with Services and Routes)
* `kong_consumer_plugin` is renamed to `kong_consumer_credential`
* `basic-auth` type of credentials are not immutable
* modules are installed into Python's `site-packages`, next to Ansible


# Requirements

- Ansible >=2.4
- ansible-dotdiff


# Usage

See [example playbook](./example/playbook.yml).


# Limitations

* There's no backward compatibility with old Kong API objects.
  If you're still using them, consider a migration to Services and Routes.
* Idempotency for `basic-auth` is work-arounded, cause it's impossible to predict an execution result,
  without comparing old password hash with the updated one without updating it in Kong.
  Existing not changed basic-auth credential will cause PATCH request to Kong on every execution.


# License

[MIT](https://github.com/Klarrio/ansible-kong-module/blob/master/LICENSE).
