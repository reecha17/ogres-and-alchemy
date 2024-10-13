from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Optional


class CreateServerForm(FlaskForm):
    create_location = StringField("location", validators=[DataRequired()])
    create_server_submit = SubmitField(
        "Create", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class UpdateServerForm(FlaskForm):
    update_serverID = IntegerField("serverID", validators=[DataRequired()])
    update_location = StringField("location", validators=[DataRequired()])
    update_server_submit = SubmitField(
        "Update", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class DeleteServerForm(FlaskForm):
    delete_serverID = IntegerField("serverID", validators=[DataRequired()])
    delete_server_submit = SubmitField(
        "Delete", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class UserForm(FlaskForm):
    create_email = StringField("email", validators=[DataRequired(), Email()])
    create_userName = StringField("userName", validators=[DataRequired()])
    create_submit = SubmitField(
        "Create", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class UpdateUserForm(FlaskForm):
    userID = IntegerField("userID", validators=[DataRequired()])
    update_email = StringField("email", validators=[DataRequired(), Email()])
    update_userName = StringField("userName", validators=[DataRequired()])
    update_submit = SubmitField(
        "Update", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class DeleteUserForm(FlaskForm):
    deleteUserID = IntegerField("userID", validators=[DataRequired()])
    update_submit = SubmitField(
        "Delete", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class CreateFactionForm(FlaskForm):
    create_factionName = StringField("factionName", validators=[DataRequired()])
    create_submit = SubmitField(
        "Create Faction", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class UpdateFactionForm(FlaskForm):
    update_factionID = IntegerField("factionID", validators=[DataRequired()])
    update_factionName = StringField("userName", validators=[DataRequired()])
    update_submit = SubmitField(
        "Update Faction", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class DeleteFactionForm(FlaskForm):
    delete_factionID = IntegerField("factionID", validators=[DataRequired()])
    delete_submit = SubmitField(
        "Delete", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class CreateWeaponForm(FlaskForm):
    create_weaponName = StringField("weaponName", validators=[DataRequired()])
    create_damage = IntegerField("damage", validators=[DataRequired()])
    create_hitpct = IntegerField("hit_pct", validators=[DataRequired()])
    create_submit = SubmitField(
        "Create", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class UpdateWeaponForm(FlaskForm):
    update_weaponID = IntegerField("weaponID", validators=[DataRequired()])
    update_weaponName = StringField("weaponName", validators=[DataRequired()])
    update_damage = IntegerField("damage", validators=[DataRequired()])
    update_hitpct = IntegerField("hit_pct", validators=[DataRequired()])
    update_submit = SubmitField(
        "Update", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class DeleteWeaponForm(FlaskForm):
    delete_weaponID = IntegerField("weaponID", validators=[DataRequired()])
    delete_submit = SubmitField(
        "Delete", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class CreateClassForm(FlaskForm):
    create_className = StringField("className", validators=[DataRequired()])
    create_submit = SubmitField(
        "Create", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class UpdateClassForm(FlaskForm):
    update_classID = IntegerField("weaponID", validators=[DataRequired()])
    update_className = StringField("className", validators=[DataRequired()])
    update_submit = SubmitField(
        "Update", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class DeleteClassForm(FlaskForm):
    delete_classID = IntegerField("weaponID", validators=[DataRequired()])
    delete_submit = SubmitField(
        "Delete", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class CreateCharacterForm(FlaskForm):
    create_characterName = StringField("characterName", validators=[DataRequired()])
    create_level = IntegerField("level", validators=[DataRequired()])
    create_userID = IntegerField("userID", validators=[DataRequired()])
    create_serverID = IntegerField("serverID", validators=[DataRequired()])
    create_classID = IntegerField("classID", validators=[DataRequired()])
    create_factionID = IntegerField("factionID", validators=[Optional()])
    create_submit = SubmitField(
        "Create", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class UpdateCharacterForm(FlaskForm):
    update_characterID = IntegerField("characterID", validators=[DataRequired()])
    update_characterName = StringField("characterName", validators=[DataRequired()])
    update_level = IntegerField("level", validators=[DataRequired()])
    update_userID = IntegerField("userID", validators=[DataRequired()])
    update_serverID = IntegerField("serverID", validators=[DataRequired()])
    update_classID = IntegerField("classID", validators=[DataRequired()])
    update_factionID = IntegerField("factionID", validators=[Optional()])
    update_submit = SubmitField(
        "Update", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )


class DeleteCharacterForm(FlaskForm):
    delete_characterID = IntegerField("level", validators=[DataRequired()])
    delete_submit = SubmitField(
        "Delete", render_kw={"class": "btn btn-outline-success my-2 my-sm-0"}
    )
