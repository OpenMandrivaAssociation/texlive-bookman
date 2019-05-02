# revision 31835
# category Package
# catalog-ctan /fonts/urw/base35
# catalog-date 2012-06-06 22:57:48 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-bookman
Version:	20190228
Release:	1
Summary:	URW "Base 35" font pack for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/urw/base35
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookman.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: - Century Schoolbook (substituting for
Adobe's New Century Schoolbook); - Dingbats (substituting for
Adobe's Zapf Dingbats); - Nimbus Mono L (substituting for
Abobe's Courier); - Nimbus Roman No9 L (substituting for
Adobe's Times); - Nimbus Sans L (substituting for Adobe's
Helvetica); - Standard Symbols L (substituting for Adobe's
Symbol); - URW Bookman; - URW Chancery L Medium Italic
(substituting for Adobe's Zapf Chancery); - URW Gothic L Book
(substituting for Adobe's Avant Garde); and - URW Palladio L
(substituting for Adobe's Palatino).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/bookman/config.ubk
%{_texmfdistdir}/fonts/afm/adobe/bookman/pbkd8a.afm
%{_texmfdistdir}/fonts/afm/adobe/bookman/pbkdi8a.afm
%{_texmfdistdir}/fonts/afm/adobe/bookman/pbkl8a.afm
%{_texmfdistdir}/fonts/afm/adobe/bookman/pbkli8a.afm
%{_texmfdistdir}/fonts/afm/urw/bookman/ubkd8a.afm
%{_texmfdistdir}/fonts/afm/urw/bookman/ubkdi8a.afm
%{_texmfdistdir}/fonts/afm/urw/bookman/ubkl8a.afm
%{_texmfdistdir}/fonts/afm/urw/bookman/ubkli8a.afm
%{_texmfdistdir}/fonts/map/dvips/bookman/ubk.map
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkd.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkd7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkd8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkd8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkd8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkdc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkdc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkdc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkdi.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkdi7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkdi8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkdi8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkdi8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkdo.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkdo7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkdo8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkdo8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkdo8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkl.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkl7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkl8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkl8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkl8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbklc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbklc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbklc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkli.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkli7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkli8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkli8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbkli8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbklo.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbklo7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbklo8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbklo8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/bookman/pbklo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkb7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkb8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkb8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkb8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkbc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkbc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkbi7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkbi8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkbi8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkbi8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkbo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkbo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkbo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkbo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkd7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkd8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkd8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkd8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkdc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkdc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkdi7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkdi8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkdi8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkdi8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkdo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkdo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkdo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkdo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkl7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkl8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkl8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkl8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubklc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubklc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkli7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkli8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkli8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkli8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubklo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubklo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubklo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubklo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkr7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkr8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkr8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkr8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkrc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkrc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkri7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkri8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkri8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkri8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkro7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkro8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkro8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/bookman/ubkro8t.tfm
%{_texmfdistdir}/fonts/type1/urw/bookman/ubkd8a.pfb
%{_texmfdistdir}/fonts/type1/urw/bookman/ubkd8a.pfm
%{_texmfdistdir}/fonts/type1/urw/bookman/ubkdi8a.pfb
%{_texmfdistdir}/fonts/type1/urw/bookman/ubkdi8a.pfm
%{_texmfdistdir}/fonts/type1/urw/bookman/ubkl8a.pfb
%{_texmfdistdir}/fonts/type1/urw/bookman/ubkl8a.pfm
%{_texmfdistdir}/fonts/type1/urw/bookman/ubkli8a.pfb
%{_texmfdistdir}/fonts/type1/urw/bookman/ubkli8a.pfm
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkd.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkd7t.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkd8c.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkd8t.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkdc.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkdc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkdc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkdi.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkdi7t.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkdi8c.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkdi8t.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkdo.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkdo7t.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkdo8c.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkdo8t.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkl.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkl7t.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkl8c.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkl8t.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbklc.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbklc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbklc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkli.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkli7t.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkli8c.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbkli8t.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbklo.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbklo7t.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbklo8c.vf
%{_texmfdistdir}/fonts/vf/adobe/bookman/pbklo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkb7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkb8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkb8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkbc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkbc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkbi7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkbi8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkbi8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkbo7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkbo8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkbo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkd7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkd8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkd8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkdc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkdc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkdi7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkdi8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkdi8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkdo7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkdo8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkdo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkl7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkl8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkl8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubklc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubklc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkli7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkli8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkli8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubklo7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubklo8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubklo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkr7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkr8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkr8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkrc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkrc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkri7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkri8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkri8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkro7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkro8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/bookman/ubkro8t.vf
%{_texmfdistdir}/tex/latex/bookman/8rubk.fd
%{_texmfdistdir}/tex/latex/bookman/omlubk.fd
%{_texmfdistdir}/tex/latex/bookman/omsubk.fd
%{_texmfdistdir}/tex/latex/bookman/ot1ubk.fd
%{_texmfdistdir}/tex/latex/bookman/t1ubk.fd
%{_texmfdistdir}/tex/latex/bookman/ts1ubk.fd

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex %{buildroot}%{_texmfdistdir}
