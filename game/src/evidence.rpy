init python:
    import copy
    evidence = None
    warrent = None
    def evidence_recorder(evidence):
        traits = [ _('Gender'), _('Hair'), _('Eyes') ]
        traits_small = {'Gender': _('gender'), 'Hair': _('hair'), 'Eyes': _('eyes') }

        choices_gender = [_('Unknown'),_('Male'),_('Female')]
        choices_hair = [_('Unknown'),_('Blond'),_('Brown'),_('Red'),_('Black')]
        choices_eyes = [_('Unknown'),_('Blue'),_('Green'),_('Brown')]

        if evidence is None:
            evidence = { _('Gender') : _('Unknown'),
                     _('Hair') : _('Unknown'),
                     _('Eyes') : _('Unknown') }

        editing = None

        def button(text, selected, returns, **properties):

            if selected:
                role='selected_'
            else:
                role=''

            ui.button(clicked=ui.returns(returns),
                      style='button', role=role, **properties)
            ui.text(text, style='button_text')

        while True:

            ui.frame(xpos=50,
                     ypos=60,
                     xanchor='left',
                     yanchor='top',
                     xfill=False,
                     xminimum=300
                     )
            ui.vbox(xpos=0.5, xanchor='center')
            ui.text("Evidence", xpos=0.5, xanchor='center', textalign=0.5)
            ui.null(height=20)

            for i in traits:
                renpy.store.traits_tmp = i
                renpy.store.evidence_tmp = evidence[i]
                button("[traits_tmp!t]: [evidence_tmp!t]", editing == i, ("edit", i), xminimum=250)

            ui.null(height=20)
            ui.textbutton(_("Return"),
                          clicked=ui.returns(("done", True)),
                          xminimum=250)
            ui.null(height=20)
            ui.close()

            ui.frame(xpos=0.5,
                     ypos=.7,
                     xanchor='center',
                     yanchor='bottom',
                     xfill=False,
                     xminimum=300
                     )

            ui.vbox(xpos=0.5, xanchor='center')

            if len(calculate_match(evidence)) > 1:
                renpy.store.criminal_matches = str(len(calculate_match(evidence)))
                ui.text(_("[criminal_matches!t] possible matches"))
            else:
                renpy.store.criminal_name = calculate_match(evidence)[0].name
                ui.text(_("{b}Match Found!{/b}"))
                ui.null(height=20)
                ui.text(_("Warrent issued for [criminal_name!t]."))
            ui.close()

            # Choice window.
            if editing:
                ui.frame(xpos=400,
                         ypos=70,
                         xanchor='left',
                         yanchor='top',
                         xfill=False,
                         xminimum=300,
                         xmargin = 10
                         )

                ui.vbox(xpos=0.5, xanchor='center')
                renpy.store.traits_small_selected = traits_small[editing]
                ui.text(_("Select [traits_small_selected!t]"),xpos=0.5, xanchor='center', textalign=0.5)
                ui.null(height=20)

                if renpy.store.traits_small_selected == 'hair':
                    for i in choices_hair:
                        button(i,
                               evidence[editing] == i,
                               ("set", i),
                               xpos=0,
                               xanchor='left',
                               xminimum=250)
                if renpy.store.traits_small_selected == 'gender':
                    for i in choices_gender:
                        button(i,
                               evidence[editing] == i,
                               ("set", i),
                               xpos=0,
                               xanchor='left',
                               xminimum=250)
                if renpy.store.traits_small_selected == 'eyes':
                    for i in choices_eyes:
                        button(i,
                               evidence[editing] == i,
                               ("set", i),
                               xpos=0,
                               xanchor='left',
                               xminimum=250)

                ui.close()

            type, value = ui.interact()

            if type == "done":
                break

            if type == "edit":
                editing = value

            if type == "set":
                evidence[editing] = value
                editing = None
                matches = calculate_match(evidence)
                criminal_matches = str(len(calculate_match(evidence)))

        return evidence

    def calculate_match(evidence):
        matches = []
        for v in villains:
            if check_trait_match(evidence['Hair'],v.hair) and check_trait_match(evidence['Eyes'],v.eyes) and check_trait_match(evidence['Gender'],v.gender):
                matches.append(copy.deepcopy(v))

        return matches

    def check_trait_match(e, v):
        return e == 'Unknown' or e == v
