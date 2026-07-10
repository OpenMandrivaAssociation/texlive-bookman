%global tl_name bookman
%global tl_revision 77161

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	URW Base 35 font pack for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/urw/base35
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bookman.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus
Mono L (substituting for Adobe's Courier); Nimbus Roman No9 L
(substituting for Adobe's Times); Nimbus Sans L (substituting for
Adobe's Helvetica); Standard Symbols L (substituting for Adobe's
Symbol); URW Bookman; URW Chancery L Medium Italic (substituting for
Adobe's Zapf Chancery); URW Gothic L Book (substituting for Adobe's
Avant Garde); and URW Palladio L (substituting for Adobe's Palatino).

%prep
%setup -q -c
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/dvips
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/dvips/bookman
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/fonts/afm/adobe
%dir %{_datadir}/texmf-dist/fonts/afm/urw
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/adobe
%dir %{_datadir}/texmf-dist/fonts/tfm/urw35vf
%dir %{_datadir}/texmf-dist/fonts/type1/urw
%dir %{_datadir}/texmf-dist/fonts/vf/adobe
%dir %{_datadir}/texmf-dist/fonts/vf/urw35vf
%dir %{_datadir}/texmf-dist/tex/latex/bookman
%dir %{_datadir}/texmf-dist/fonts/afm/adobe/bookman
%dir %{_datadir}/texmf-dist/fonts/afm/urw/bookman
%dir %{_datadir}/texmf-dist/fonts/map/dvips/bookman
%dir %{_datadir}/texmf-dist/fonts/tfm/adobe/bookman
%dir %{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman
%dir %{_datadir}/texmf-dist/fonts/type1/urw/bookman
%dir %{_datadir}/texmf-dist/fonts/vf/adobe/bookman
%dir %{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman
%{_datadir}/texmf-dist/dvips/bookman/config.ubk
%{_datadir}/texmf-dist/fonts/afm/adobe/bookman/pbkd8a.afm
%{_datadir}/texmf-dist/fonts/afm/adobe/bookman/pbkdi8a.afm
%{_datadir}/texmf-dist/fonts/afm/adobe/bookman/pbkl8a.afm
%{_datadir}/texmf-dist/fonts/afm/adobe/bookman/pbkli8a.afm
%{_datadir}/texmf-dist/fonts/afm/urw/bookman/ubkd8a.afm
%{_datadir}/texmf-dist/fonts/afm/urw/bookman/ubkdi8a.afm
%{_datadir}/texmf-dist/fonts/afm/urw/bookman/ubkl8a.afm
%{_datadir}/texmf-dist/fonts/afm/urw/bookman/ubkli8a.afm
%{_datadir}/texmf-dist/fonts/map/dvips/bookman/ubk.map
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkd.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkd7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkd8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkd8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkd8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkdc.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkdc7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkdc8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkdi.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkdi7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkdi8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkdi8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkdi8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkdo.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkdo7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkdo8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkdo8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkdo8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkl.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkl7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkl8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkl8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkl8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbklc.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbklc7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbklc8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkli.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkli7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkli8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkli8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbkli8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbklo.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbklo7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbklo8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbklo8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/bookman/pbklo8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkb7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkb8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkb8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkb8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkbc7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkbc8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkbi7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkbi8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkbi8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkbi8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkbo7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkbo8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkbo8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkbo8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkd7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkd8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkd8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkd8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkdc7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkdc8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkdi7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkdi8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkdi8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkdi8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkdo7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkdo8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkdo8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkdo8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkl7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkl8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkl8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkl8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubklc7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubklc8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkli7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkli8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkli8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkli8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubklo7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubklo8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubklo8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubklo8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkr7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkr8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkr8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkr8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkrc7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkrc8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkri7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkri8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkri8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkri8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkro7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkro8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkro8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/bookman/ubkro8t.tfm
%{_datadir}/texmf-dist/fonts/type1/urw/bookman/ubkd8a.pfb
%{_datadir}/texmf-dist/fonts/type1/urw/bookman/ubkd8a.pfm
%{_datadir}/texmf-dist/fonts/type1/urw/bookman/ubkdi8a.pfb
%{_datadir}/texmf-dist/fonts/type1/urw/bookman/ubkdi8a.pfm
%{_datadir}/texmf-dist/fonts/type1/urw/bookman/ubkl8a.pfb
%{_datadir}/texmf-dist/fonts/type1/urw/bookman/ubkl8a.pfm
%{_datadir}/texmf-dist/fonts/type1/urw/bookman/ubkli8a.pfb
%{_datadir}/texmf-dist/fonts/type1/urw/bookman/ubkli8a.pfm
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkd.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkd7t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkd8c.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkd8t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkdc.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkdc7t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkdc8t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkdi.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkdi7t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkdi8c.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkdi8t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkdo.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkdo7t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkdo8c.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkdo8t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkl.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkl7t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkl8c.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkl8t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbklc.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbklc7t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbklc8t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkli.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkli7t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkli8c.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbkli8t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbklo.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbklo7t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbklo8c.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/bookman/pbklo8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkb7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkb8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkb8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkbc7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkbc8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkbi7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkbi8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkbi8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkbo7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkbo8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkbo8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkd7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkd8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkd8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkdc7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkdc8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkdi7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkdi8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkdi8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkdo7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkdo8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkdo8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkl7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkl8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkl8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubklc7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubklc8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkli7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkli8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkli8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubklo7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubklo8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubklo8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkr7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkr8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkr8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkrc7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkrc8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkri7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkri8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkri8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkro7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkro8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/bookman/ubkro8t.vf
%{_datadir}/texmf-dist/tex/latex/bookman/8rubk.fd
%{_datadir}/texmf-dist/tex/latex/bookman/omlubk.fd
%{_datadir}/texmf-dist/tex/latex/bookman/omsubk.fd
%{_datadir}/texmf-dist/tex/latex/bookman/ot1ubk.fd
%{_datadir}/texmf-dist/tex/latex/bookman/t1ubk.fd
%{_datadir}/texmf-dist/tex/latex/bookman/ts1ubk.fd
