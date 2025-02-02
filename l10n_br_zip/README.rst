================================
Brazilian Localisation ZIP Codes
================================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fl10n--brazil-lightgray.png?logo=github
    :target: https://github.com/OCA/l10n-brazil/tree/14.0/l10n_br_zip
    :alt: OCA/l10n-brazil
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/l10n-brazil-14-0/l10n-brazil-14-0-l10n_br_zip
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runbot-Try%20me-875A7B.png
    :target: https://runbot.odoo-community.org/runbot/124/14.0
    :alt: Try me on Runbot

|badge1| |badge2| |badge3| |badge4| |badge5| 


**Table of contents**

.. contents::
   :local:

Installation
============

Este módulo depende do l10n_br_base e da biblioteca PyCEP-Correios.

Configuration
=============

Ao ser instalado o módulo de CEP deve ser populado a tabela l10n_br.zip ou quando o CEP não for encontrado ele será consultado no serviço dos Correios utilizando a biblioteca PyCEP-Correios.

Usage
=====

Nos endereços de parceiro, empresa e prospectos será exibido ao lado do campo CEP um botão para pesquisa de CEP.

Changelog
=========

12.0.2.0.0 (2019-06-17)
~~~~~~~~~~~~~~~~~~~~~~~

 * [REF] Incluida pesquisa e dependência da biblioteca PyCEP-Correios.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/l10n-brazil/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/OCA/l10n-brazil/issues/new?body=module:%20l10n_br_zip%0Aversion:%2014.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Akretion

Contributors
~~~~~~~~~~~~

* `Akretion <https://www.akretion.com>`_:

  * Renato Lima <renato.lima@akretion.com.br>
  * Magno Costa <magno.costa@akretion.com.br>
* `KMEE <https://www.kmee.com.br>`_:

  * Hendrix Costa <hendrix.costa@kmee.com.br>
  * Luis Felipe Mileo <mileo@kmee.com.br>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-renatonlima| image:: https://github.com/renatonlima.png?size=40px
    :target: https://github.com/renatonlima
    :alt: renatonlima
.. |maintainer-mbcosta| image:: https://github.com/mbcosta.png?size=40px
    :target: https://github.com/mbcosta
    :alt: mbcosta
.. |maintainer-mileo| image:: https://github.com/mileo.png?size=40px
    :target: https://github.com/mileo
    :alt: mileo

Current `maintainers <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-renatonlima| |maintainer-mbcosta| |maintainer-mileo| 

This module is part of the `OCA/l10n-brazil <https://github.com/OCA/l10n-brazil/tree/14.0/l10n_br_zip>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
