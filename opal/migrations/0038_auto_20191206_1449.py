# Generated by Django 2.0.13 on 2019-12-06 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0037_auto_20181114_1445'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Line_complication',
        ),
        migrations.DeleteModel(
            name='Line_removal_reason',
        ),
        migrations.DeleteModel(
            name='Line_site',
        ),
        migrations.DeleteModel(
            name='Line_type',
        ),
        migrations.DeleteModel(
            name='Macro',
        ),
        migrations.DeleteModel(
            name='Micro_test_c_difficile',
        ),
        migrations.DeleteModel(
            name='Micro_test_csf_pcr',
        ),
        migrations.DeleteModel(
            name='Micro_test_ebv_serology',
        ),
        migrations.DeleteModel(
            name='Micro_test_hepititis_b_serology',
        ),
        migrations.DeleteModel(
            name='Micro_test_hiv',
        ),
        migrations.DeleteModel(
            name='Micro_test_leishmaniasis_pcr',
        ),
        migrations.DeleteModel(
            name='Micro_test_mcs',
        ),
        migrations.DeleteModel(
            name='Micro_test_other',
        ),
        migrations.DeleteModel(
            name='Micro_test_parasitaemia',
        ),
        migrations.DeleteModel(
            name='Micro_test_respiratory_virus_pcr',
        ),
        migrations.DeleteModel(
            name='Micro_test_serology',
        ),
        migrations.DeleteModel(
            name='Micro_test_single_igg_test',
        ),
        migrations.DeleteModel(
            name='Micro_test_single_test_pos_neg',
        ),
        migrations.DeleteModel(
            name='Micro_test_single_test_pos_neg_equiv',
        ),
        migrations.DeleteModel(
            name='Micro_test_stool_parasitology_pcr',
        ),
        migrations.DeleteModel(
            name='Micro_test_stool_pcr',
        ),
        migrations.DeleteModel(
            name='Micro_test_swab_pcr',
        ),
        migrations.DeleteModel(
            name='Micro_test_syphilis_serology',
        ),
        migrations.DeleteModel(
            name='Micro_test_viral_load',
        ),
        migrations.DeleteModel(
            name='Microbiology_organism',
        ),
    ]
