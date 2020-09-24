# -*- ISO-8859-1 -*-
#
# file: aplicativo.py
#
# Created by Cleber Almeida Pereira
# e-mail: cleber.ap.desenvolvedor@gmail.com
#
# programming language: Python v3.7.0
#

from container import Container
#from os.path import join, dirname
#from pathlib import Path
from PIL import ImageTk, Image
from tkinter import font
from tkinter import ttk
from sys import platform
from Algorithm import *
#import configparser
import csv
import gettext
#import locale
#import logging
import os
import random
import tkinter as tk
#import tkinter.colorchooser
import tkinter.filedialog as fdlg
import tkinter.messagebox as tkmsg
import tkinter.scrolledtext as tkst
#import tkinter.simpledialog
import sys

_ = gettext.gettext

class meu_Aplicativo:
    def __init__(self, **kw):
        self.root = tk.Tk()
        self.root.title('BestContainers - O Melhor Aproveitamento de Recipientes')
        self.root.geometry('980x600')

        
        # Definition of variables and constants
        self.max_capacity = 1000.00
        self.increment = 0.01
        # Define a variável "Flag" que indica o índice do recipiente principal (que será preenchido) selecionado
        self.index_main_selected = -1
        # Lista de containers principais
        self.list_containers_main = []
        # Lista de conteiners que serão descarregados
        self.list_containers_dumped = []
        # Lista de tipos de recipiente
        self.list_container_types = ['bombona', 'galão', 'garrafa', 'garrafão', 'reservatório', 'tanque']
        # Lista de unidades de medida para líquidos
        self.list_measure = ['(dl) - decilitro', '(cl) - centilitro', '(ml) - mililitro', '(l) - litro', '(kl) - quilolitro', '(hl) - hectolitro', '(dal) - decalitro']
        # Lista de materiais utilizados na fabricação de galão
        self.list_container_materials = ['PET', 'policarbonato', 'polietileno tereftalato', 'polipropileno', 'pp']
        # Lista de tipos de conteúdo do galão
        self.list_contents = ['água', 'detergente', 'gasolina', 'óleo', 'sabão']
        # Lista de marcas
        self.list_brands = ['Marca1', 'Marca2', 'Marca3', 'Marca4'] 

        self.create_menu()
        self.create_area()

        # Define o recipiente principal
        #self.define_container_main()

        #gripObj = ttk.Sizegrip(self.root)
        #gripObj.pack(side= 'right', anchor= 'se')

    # Área principal
    def create_area(self):
        self.mainframe = ttk.Frame(master=self.root)

        # Frame Esquerdo - Recipientes Principais
        self.frm_e = tk.Frame(self.mainframe)
        self.frm_e.grid(row=0, column=0, padx=5, pady=5, stick='nwe')
        
        # Frame Meio - Recipientes que serão descarregados
        self.frm_m = tk.Frame(self.mainframe)
        self.frm_m.grid(row=0, column=1, padx=5, pady=5, stick='nwe')
        
        # Frame Direito - Análises
        self.frm_d = tk.Frame(self.mainframe)
        self.frm_d.grid(row=0, column=2, padx=5, pady=5, stick='nwe')

        ## Frame Esquerdo - Widgets **********************************************************************************************
        btn_add_container_main = tk.Button(self.frm_e, text='Adicionar Recipiente Principal', font=font.Font(size=10, weight='bold'), command=self.define_container_main)
        btn_add_container_main.configure(bg='#cccccc')
        btn_add_container_main.grid(row=0, column=0, columnspan=5, padx=5, pady=5, ipadx=5, ipady=5)

        sep_e_1 = ttk.Separator(self.frm_e, orient='horizontal')
        sep_e_1.grid(row=1, column=0, columnspan=34, padx=5, pady=10, stick='we')

        # ListBox de recipientes Principais
        lbl_list_containers_main = tk.Label(self.frm_e, text="Recipientes Principais", font=font.Font(size=10, weight='bold'))
        lbl_list_containers_main.grid(row=2, column=0, padx=5, pady=5, stick='w')
        
        self.lbx_containers_main = tk.Listbox(self.frm_e, height=15, selectmode=tk.SINGLE)
        self.lbx_containers_main.grid(row=3, column=0, columnspan=4, padx=5, sticky='we')
        
        # Se há registros para inserção
        if len(self.list_containers_main) > 0:
            for item in self.list_containers_main:
                self.lbx_containers_main.insert(tk.END, item.get_info())

        self.sbar_V_cont_main = tk.Scrollbar(self.frm_e, orient=tk.VERTICAL, command=self.lbx_containers_main.yview)
        self.sbar_H_cont_main = tk.Scrollbar(self.frm_e, orient=tk.HORIZONTAL, command=self.lbx_containers_main.xview)
        self.lbx_containers_main.configure(yscrollcommand=self.sbar_V_cont_main.set)
        self.lbx_containers_main.configure(xscrollcommand=self.sbar_H_cont_main.set)
        self.sbar_V_cont_main.grid(row=3, column=4, stick='ns')
        self.sbar_H_cont_main.grid(row=4, column=0, columnspan=4, stick='we')

        # instrução DESABILITADA. Considerada desnecessária
        self.lbx_containers_main.bind("<<ListboxSelect>>", self.view_container_main)

        sep_e_2 = ttk.Separator(self.frm_e, orient='horizontal')
        sep_e_2.grid(row=5, column=0, columnspan=34, padx=5, pady=10, stick='we')

        #Limpar Listbox
        btn_clear_lbx_containers_main = tk.Button(self.frm_e, text='Limpar Lista', font=font.Font(size=10, weight='bold'), command=self.clear_lbx_containers_main)
        btn_clear_lbx_containers_main.configure(bg='#cccccc')
        btn_clear_lbx_containers_main.grid(row=6, column=0, columnspan=4, padx=5, pady=5, stick='we')

        ## Frame Esquerdo - Widgets **** FIM *************************************************************************************
        

        ## Frame Meio - Widgets **************************************************************************************************
        btn_add_container_dumped = tk.Button(self.frm_m, text='Adicionar Recipiente de Despejo', font=font.Font(size=10, weight='bold'), command=self.menu_container_dumped)
        btn_add_container_dumped.configure(bg='#cccccc')
        btn_add_container_dumped.grid(row=0, column=0, columnspan=5, padx=5, pady=5, ipadx=5, ipady=5)

        sep_m_1 = ttk.Separator(self.frm_m, orient='horizontal')
        sep_m_1.grid(row=1, column=0, columnspan=4, padx=5, pady=10, stick='we')

        # ListBox de recipientes cujo conteúdo será despejado no recipiente principal selecionado
        lbl_list_containers_dumped = tk.Label(self.frm_m, text="Recipientes de Despejo", font=font.Font(size=10, weight='bold'))
        lbl_list_containers_dumped.grid(row=2, column=0, padx=5, pady=5, stick='w')
        
        self.lbx_containers_dumped = tk.Listbox(self.frm_m, height=15)
        self.lbx_containers_dumped.grid(row=3, column=0, columnspan=4, padx=5, sticky='we')
        self.lbx_containers_dumped.configure(selectmode='extended')

        # Se há registros para inserção
        if len(self.list_containers_dumped) > 0:
            for item in self.list_containers_dumped:
                self.lbx_containers_dumped.insert(tk.END, item.get_info())

        self.sbar_V_cont_dumped = tk.Scrollbar(self.frm_m, orient=tk.VERTICAL, command=self.lbx_containers_dumped.yview)
        self.sbar_H_cont_dumped = tk.Scrollbar(self.frm_m, orient=tk.HORIZONTAL, command=self.lbx_containers_dumped.xview)
        self.lbx_containers_dumped.configure(yscrollcommand=self.sbar_V_cont_dumped.set)
        self.lbx_containers_dumped.configure(xscrollcommand=self.sbar_H_cont_dumped.set)
        self.sbar_V_cont_dumped.grid(row=3, column=4, stick='ns')
        self.sbar_H_cont_dumped.grid(row=4, column=0, columnspan=4, stick='we')

        # instrução DESABILITADA. Considerada desnecessária
        self.lbx_containers_dumped.bind("<<ListboxSelect>>", self.view_container_dumped)

        sep_m_2 = ttk.Separator(self.frm_m, orient='horizontal')
        sep_m_2.grid(row=5, column=0, columnspan=4, padx=5, pady=10, stick='we')

        #Limpar Listbox
        btn_clear_lbx_containers_dumped = tk.Button(self.frm_m, text='Limpar Lista', font=font.Font(size=10, weight='bold'), command=self.clear_lbx_containers_dumped)
        btn_clear_lbx_containers_dumped.configure(bg="#cccccc")
        btn_clear_lbx_containers_dumped.grid(row=6, column=0, columnspan=4, padx=5, pady=5, stick='we')
        ## Frame Meio - Widgets **** FIM *****************************************************************************************


        ## Frame Direito - Widgets ***********************************************************************************************
        btn_analysis = tk.Button(self.frm_d, text='Analisar Possibilidades', font=font.Font(size=10, weight='bold'), command=self.analysis)
        btn_analysis.configure(bg='#cccccc')
        btn_analysis.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipadx=5, ipady=5, stick='we')
        #btn_analysis.configure(state='disabled')

        btn_analysis_selecteds = tk.Button(self.frm_d, text='Analisar Selecionados', font=font.Font(size=10, weight='bold'), command=self.analysis_selecteds)
        btn_analysis_selecteds.configure(bg='#cccccc')
        btn_analysis_selecteds.grid(row=1, column=0, columnspan=4, padx=5, pady=5, ipadx=5, ipady=5, stick='we')

        self.lblfrm_resultados = tk.LabelFrame(self.frm_d, text='Resultados')
        self.lblfrm_resultados.grid(row=2, column=0, columnspan=4, padx=5, pady=10,stick='nwes')

        ## Frame Direito - Widgets **** FIM **************************************************************************************
        
        self.mainframe.grid(row=0, column=0)


    def create_menu(self):
        mnu_bar = tk.Menu(self.root)
        self.root.config(menu=mnu_bar)
        self.file_mnu = tk.Menu(mnu_bar, tearoff=0)

        self.export_mnu = tk.Menu(self.file_mnu, tearoff=0)
        self.export_mnu.add_command(label=_("*.CSV"), command=self.export_csv)
        self.file_mnu.add_cascade(label=_("Export"), menu=self.export_mnu)

        self.import_mnu = tk.Menu(self.file_mnu, tearoff=0)
        self.import_mnu.add_command(label=_("*.CSV"), command=self.import_csv)
        self.file_mnu.add_cascade(label=_("Import"), menu=self.import_mnu)

        self.file_mnu.add_separator()

        self.file_mnu.add_command(label=_("Exit"), command=self.end_app)
        mnu_bar.add_cascade(label=_("File"), menu=self.file_mnu)

        
    def end_app(self):
        self.root.quit()

    def execute(self):
        self.root.mainloop()

    # Tela 1 - Define um container principal
    def define_container_main(self, container_type=1, registry='', capacity=0, measure=3, material=-1, content=0, brand=-1 ):
        window = tk.Toplevel(self.root)
        window.wm_title('Registro do Recipiente Principal')
        window.transient(self.root)
        window.grab_set()

        window_frm = tk.Frame(window)
        window_frm.grid(row=0, column=0, padx=10, pady=10, stick='nw')
        
        # Tipo do Recipiente
        lbl_container_type = tk.Label(window_frm, text='Tipo:', font=font.Font(size=10, weight='bold'))
        lbl_container_type.grid(row=0, column=0, padx=5, pady=5, stick='w')

        self.cbbox_container_type = ttk.Combobox(window_frm, values=self.list_container_types)
        self.cbbox_container_type.grid(row=0, column=1, columnspan=2, padx=5, pady=5, stick='we')
        self.cbbox_container_type.current(container_type)

        # Identificação de Registro
        lbl_registry = tk.Label(window_frm, text='Registro nº:', font=font.Font(size=10, weight='bold'))
        lbl_registry.grid(row=1, column=0, padx=5, pady=5, stick='w')
        
        self.registry_var = tk.StringVar()
        self.registry_var.set(registry)
        input_registry = tk.Entry(window_frm, justify='center', textvariable=self.registry_var)
        input_registry.focus()
        input_registry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, ipadx=3, ipady=3, stick='we')

        # Capacidade
        lbl_capacity = tk.Label(window_frm, text='Capacidade:', font=font.Font(size=10, weight='bold'))
        lbl_capacity.grid(row=2, column=0, padx=5, pady=5, stick='w')
        
        self.capacity_var = tk.DoubleVar()
        self.capacity_var.set(capacity)
        input_capacity = ttk.Spinbox(window_frm,
                                     width=10,
                                     justify='center',
                                     from_=0.00,
                                     to=self.max_capacity,
                                     textvariable=self.capacity_var,
                                     increment=self.increment)
        input_capacity.grid(row=2, column=1, padx=5, pady=5, stick='w')

        # Unidade de medida
        lbl_measure = tk.Label(window_frm, text='Grandeza:', font=font.Font(size=10, weight='bold'))
        lbl_measure.grid(row=2, column=2, padx=10, pady=5, stick='e')

        self.cbbox_measure = ttk.Combobox(window_frm, width=15, values=self.list_measure)
        self.cbbox_measure.grid(row=2, column=3, padx=5, pady=5, sticky='w')
        self.cbbox_measure.current(measure)

        # Tipo de material do recipiente
        lbl_container_material = tk.Label(window_frm, text='Material do Recipiente:', font=font.Font(size=10, weight='bold'))
        lbl_container_material.grid(row=3, column=0, padx=5, pady=5, stick='w')

        self.cbbox_material = ttk.Combobox(window_frm, values=self.list_container_materials)
        self.cbbox_material.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky='we')
        if material > -1:
            self.cbbox_material.current(material)

        # Conteúdo do galão
        lbl_content = tk.Label(window_frm, text="Conteúdo:", font=font.Font(size=10, weight='bold'))
        lbl_content.grid(row=4, column=0, padx=5, pady=5, stick='w')

        self.cbbox_content = ttk.Combobox(window_frm, values=self.list_contents)
        self.cbbox_content.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky='we')
        self.cbbox_content.current(content)

        # Marca
        lbl_brand = tk.Label(window_frm, text="Marca:", font=font.Font(size=10, weight='bold'))
        lbl_brand.grid(row=5, column=0, padx=5, pady=5, stick='w')

        self.cbbox_brand = ttk.Combobox(window_frm, values=self.list_brands)
        self.cbbox_brand.grid(row=5, column=1, columnspan=3, padx=5, pady=5, sticky='we')
        if brand > -1:
            self.cbbox_brand.current(brand)

        sep = ttk.Separator(window_frm, orient='horizontal')
        sep.grid(row=6, column=0, columnspan=4, padx=5, pady=10, stick='we')

        # Botão
        btn_register = tk.Button(window_frm, text='Registrar', font=font.Font(size=10, weight='bold'), command= lambda: (self.create_container_main(), window.destroy()))
        btn_register.configure(bg='#cccccc')
        btn_register.grid(row=7, column=0, columnspan=4, padx=5, pady=5)


    def create_container_main(self):
        # 1ª Verificação - identificação do recipiente.
        if self.registry_var.get() == '':
            tkmsg.showwarning('Aviso','O campo de registro deve ser preenchido')
            self.define_container_main(self.cbbox_container_type.current(), self.registry_var.get(), self.capacity_var.get(), self.cbbox_measure.current(), self.cbbox_material.current(), self.cbbox_content.current(), self.cbbox_brand.current())
        else:
            # 2ª Verificação - capacidade do recipiente.
            if self.capacity_var.get() == 0:
                tkmsg.showwarning('Aviso','A capacidade do recipiente deve ser maior que zero')
                self.define_container_main(self.cbbox_container_type.current(), self.registry_var.get(), self.capacity_var.get(), self.cbbox_measure.current(), self.cbbox_material.current(), self.cbbox_content.current(), self.cbbox_brand.current())
            else:
                # 3ª Verificação - duplicidade
                # *** IMPORTANTÍSSIMO
                # Antes de criar o objeto o nome deste deve ser verificado com os demais da lista para evitar duplicidade
                if self.check_duplicity_main():
                    #print('Será criado o objeto', self.registry_var.get())
                    container_main = Container(self.capacity_var.get(), self.cbbox_container_type.get(), self.cbbox_content.get(), self.cbbox_measure.get(), self.registry_var.get(), self.cbbox_material.get(), self.cbbox_brand.get())

                    self.list_containers_main.append(container_main)

                    self.lbx_containers_main.insert(tk.END, container_main.get_info_dict())
                else:
                    tkmsg.showwarning('Aviso','Já existe um recipiente com este registro.')
                    self.define_container_main(self.cbbox_container_type.current(), self.registry_var.get(), self.capacity_var.get(), self.cbbox_measure.current(), self.cbbox_material.current(), self.cbbox_content.current(), self.cbbox_brand.current())

    # obtem o índice do Recipiente Principal. Apenas um por vez
    def view_container_main(self, event):
        try:
            self.index_main_selected = self.lbx_containers_main.curselection()[0]
            #container = self.lbx_containers_main.get(index_selected)
            #print(container)
            #self.clear_lbox_selection()
        except:
            pass

    def clear_lbx_containers_main(self):
        self.list_containers_main.clear()
        self.lbx_containers_main.delete(0, tk.END)

    def check_duplicity_main(self):
        flag = True

        for container in self.list_containers_main:
            if container.get_registry() == self.registry_var.get():
                flag = False
                break

        return flag

    # Tela 2 - Define um container de despejo
    def menu_container_dumped(self):
        window = tk.Toplevel(self.root)
        window.wm_title('Escolha uma opção de criação.')
        window.transient(self.root)
        window.grab_set()

        window_frm = tk.Frame(window)
        window_frm.grid(row=0, column=0, padx=10, pady=10, stick='nw')
        
        # Novo
        btn_new = tk.Button(window_frm, text='Novo', font=font.Font(size=10, weight='bold'), command= lambda: (self.define_container_dumped(), window.destroy()))
        btn_new.configure(bg='#cccccc')
        btn_new.grid(row=0, column=0, padx=5, pady=5, ipadx=5, ipady=5, stick='we')

        # Gerar automaticamente
        btn_automatic = tk.Button(window_frm, text='Gerar Registros Automaticamente', font=font.Font(size=10, weight='bold'), command=lambda: (self.create_dump_automatically_menu(), window.destroy()))
        btn_automatic.configure(bg='#cccccc')
        btn_automatic.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5, stick='we')

    
    def define_container_dumped(self, container_type=2, registry='', capacity=0, measure=3, material=-1, content=0, brand=-1 ):
        window = tk.Toplevel(self.root)
        window.wm_title('Registro de Recipiente de Despejo')
        window.transient(self.root)
        window.grab_set()

        window_frm = tk.Frame(window)
        window_frm.grid(row=0, column=0, padx=10, pady=10, stick='nw')
        
        # Tipo do Recipiente
        lbl_container_type = tk.Label(window_frm, text='Tipo:', font=font.Font(size=10, weight='bold'))
        lbl_container_type.grid(row=0, column=0, padx=5, pady=5, stick='w')

        self.cbbox_container_type = ttk.Combobox(window_frm, values=self.list_container_types)
        self.cbbox_container_type.grid(row=0, column=1, columnspan=2, padx=5, pady=5, stick='we')
        self.cbbox_container_type.current(container_type)

        # Identificação de Registro
        lbl_registry = tk.Label(window_frm, text='Registro nº:', font=font.Font(size=10, weight='bold'))
        lbl_registry.grid(row=1, column=0, padx=5, pady=5, stick='w')
        
        self.registry_var = tk.StringVar()
        self.registry_var.set(registry)
        input_registry = tk.Entry(window_frm, justify='center', textvariable=self.registry_var)
        input_registry.focus()
        input_registry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, ipadx=3, ipady=3, stick='we')

        # Capacidade
        lbl_capacity = tk.Label(window_frm, text='Capacidade:', font=font.Font(size=10, weight='bold'))
        lbl_capacity.grid(row=2, column=0, padx=5, pady=5, stick='w')
        
        self.capacity_var = tk.DoubleVar()
        self.capacity_var.set(capacity)
        input_capacity = ttk.Spinbox(window_frm,
                                     width=10,
                                     justify='center',
                                     from_=0.00,
                                     to=self.max_capacity,
                                     textvariable=self.capacity_var,
                                     increment=self.increment)
        input_capacity.grid(row=2, column=1, padx=5, pady=5, stick='w')

        # Unidade de medida
        lbl_measure = tk.Label(window_frm, text='Grandeza:', font=font.Font(size=10, weight='bold'))
        lbl_measure.grid(row=2, column=2, padx=10, pady=5, stick='e')

        self.cbbox_measure = ttk.Combobox(window_frm, width=15, values=self.list_measure)
        self.cbbox_measure.grid(row=2, column=3, padx=5, pady=5, sticky='w')
        self.cbbox_measure.current(measure)

        # Tipo de material do recipiente
        lbl_container_material = tk.Label(window_frm, text='Material do Recipiente:', font=font.Font(size=10, weight='bold'))
        lbl_container_material.grid(row=3, column=0, padx=5, pady=5, stick='w')

        self.cbbox_material = ttk.Combobox(window_frm, values=self.list_container_materials)
        self.cbbox_material.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky='we')
        if material > -1:
            self.cbbox_material.current(material)

        # Conteúdo do galão
        lbl_content = tk.Label(window_frm, text="Conteúdo:", font=font.Font(size=10, weight='bold'))
        lbl_content.grid(row=4, column=0, padx=5, pady=5, stick='w')

        self.cbbox_content = ttk.Combobox(window_frm, values=self.list_contents)
        self.cbbox_content.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky='we')
        self.cbbox_content.current(content)

        # Marca
        lbl_brand = tk.Label(window_frm, text="Marca:", font=font.Font(size=10, weight='bold'))
        lbl_brand.grid(row=5, column=0, padx=5, pady=5, stick='w')

        self.cbbox_brand = ttk.Combobox(window_frm, values=self.list_brands)
        self.cbbox_brand.grid(row=5, column=1, columnspan=3, padx=5, pady=5, sticky='we')
        if brand > -1:
            self.cbbox_brand.current(brand)

        sep = ttk.Separator(window_frm, orient='horizontal')
        sep.grid(row=6, column=0, columnspan=4, padx=5, pady=10, stick='we')

        # Botão
        btn_register = tk.Button(window_frm, text='Registrar', font=font.Font(size=10, weight='bold'), command= lambda: (self.create_container_dumped(), window.destroy()))
        btn_register.configure(bg='#cccccc')
        btn_register.grid(row=7, column=0, columnspan=4, padx=5, pady=5)


    def create_container_dumped(self):
        # 1ª Verificação - identificação do recipiente.
        if self.registry_var.get() == '':
            tkmsg.showwarning('Aviso','O campo de registro deve ser preenchido')
            self.define_container_dumped(self.cbbox_container_type.current(), self.registry_var.get(), self.capacity_var.get(), self.cbbox_measure.current(), self.cbbox_material.current(), self.cbbox_content.current(), self.cbbox_brand.current())
        else:
            # 2ª Verificação - capacidade do recipiente.
            if self.capacity_var.get() == 0:
                tkmsg.showwarning('Aviso','A capacidade do recipiente deve ser maior que zero')
                self.define_container_dumped(self.cbbox_container_type.current(), self.registry_var.get(), self.capacity_var.get(), self.cbbox_measure.current(), self.cbbox_material.current(), self.cbbox_content.current(), self.cbbox_brand.current())
            else:
                # 3ª Verificação - duplicidade
                # *** IMPORTANTÍSSIMO
                # Antes de criar o objeto o nome deste deve ser verificado com os demais da lista para evitar duplicidade
                if self.check_duplicity_dumped():
                    #print('Será criado o objeto', self.registry_var.get())
                    container_dumped = Container(self.capacity_var.get(), self.cbbox_container_type.get(), self.cbbox_content.get(), self.cbbox_measure.get(), self.registry_var.get(), self.cbbox_material.get(), self.cbbox_brand.get())

                    self.list_containers_dumped.append(container_dumped)

                    self.lbx_containers_dumped.insert(tk.END, container_dumped.get_info_dict())
                else:
                    tkmsg.showwarning('Aviso','Já existe um recipiente com este registro.')
                    self.define_container_dumped(self.cbbox_container_type.current(), self.registry_var.get(), self.capacity_var.get(), self.cbbox_measure.current(), self.cbbox_material.current(), self.cbbox_content.current(), self.cbbox_brand.current())

    # instrução que chama foi DESABILITADA. Considerada desnecessária
    def view_container_dumped(self, event):
        try:
            #index_selected = self.lbx_containers_dumped.curselection()[0]
            #container = self.lbx_containers_dumped.get(index_selected)
            #print(container)
            #self.clear_lbox_selection()
            if self.index_main_selected > -1:
                self.lbx_containers_main.itemconfig(self.index_main_selected, background='black', foreground='white')
        except:
            pass

    def clear_lbx_containers_dumped(self):
        self.list_containers_dumped.clear()
        self.lbx_containers_dumped.delete(0, tk.END)

    def check_duplicity_dumped(self):
        flag = True

        for container in self.list_containers_dumped:
            if container.get_registry() == self.registry_var.get():
                flag = False
                break

        return flag

    #def create_dump_automatically_menu(self, container_type_ini=2, registry_ini='', capacity_min=0, capacity_max=0, measure_ini=3, material_ini=-1, content_ini=0, brand_ini=-1 )):
    def create_dump_automatically_menu(self, container_type_ini=2, registry_ini='', capacity_min=0.01, capacity_max=10, measure_ini=3, content_ini=0):
        window = tk.Toplevel(self.root)
        window.wm_title('Defina os padrões de geração')
        window.transient(self.root)
        window.grab_set()

        window_frm = tk.Frame(window)
        window_frm.grid(row=0, column=0, padx=10, pady=10, stick='nw')
        
        # Quantidade de registros a criar
        lbl_qtd = tk.Label(window_frm, text='Quantidade a ser gerada:', font=font.Font(size=10, weight='bold'))
        lbl_qtd.grid(row=0, column=0, padx=5, pady=5, stick='w')
        self.qtd_var = tk.IntVar()
        self.qtd_var.set(1)
        input_qtd = tk.Entry(window_frm, justify='center', textvariable=self.qtd_var)
        input_qtd.focus()
        input_qtd.grid(row=0, column=1, padx=5, pady=5, stick='w')
        
        # Tipo do Recipiente
        lbl_container_type_ini = tk.Label(window_frm, text='Tipo:', font=font.Font(size=10, weight='bold'))
        lbl_container_type_ini.grid(row=1, column=0, padx=5, pady=5, stick='w')

        self.cbbox_container_type_ini = ttk.Combobox(window_frm, values=self.list_container_types)
        self.cbbox_container_type_ini.grid(row=1, column=1, columnspan=2, padx=5, pady=5, stick='we')
        self.cbbox_container_type_ini.current(container_type_ini)

        # número inicial de registro
        lbl_registry_ini = tk.Label(window_frm, text='Nº de registro inicial:', font=font.Font(size=10, weight='bold'))
        lbl_registry_ini.grid(row=2, column=0, padx=5, pady=5, stick='w')

        self.registry_ini_var = tk.StringVar()
        self.registry_ini_var.set(registry_ini)
        input_registry_ini = tk.Entry(window_frm, justify='center', textvariable=self.registry_ini_var)
        input_registry_ini.grid(row=2, column=1, columnspan=3, padx=5, pady=5, ipadx=3, ipady=3, stick='we')

        # Capacidade Mínima
        lbl_capacity_min = tk.Label(window_frm, text='Capacidade mínima:', font=font.Font(size=10, weight='bold'))
        lbl_capacity_min.grid(row=3, column=0, padx=5, pady=5, stick='w')
        
        self.capacity_min_var = tk.DoubleVar()
        self.capacity_min_var.set(capacity_min)
        input_capacity_min = ttk.Spinbox(window_frm,
                                     width=10,
                                     justify='center',
                                     from_=0.00,
                                     to=self.max_capacity,
                                     textvariable=self.capacity_min_var,
                                     increment=self.increment)
        input_capacity_min.grid(row=3, column=1, padx=5, pady=5, stick='w')

        # Capacidade Máxima
        lbl_capacity_max = tk.Label(window_frm, text='Capacidade máxima:', font=font.Font(size=10, weight='bold'))
        lbl_capacity_max.grid(row=4, column=0, padx=5, pady=5, stick='w')
        
        self.capacity_max_var = tk.DoubleVar()
        self.capacity_max_var.set(capacity_max)
        input_capacity_max = ttk.Spinbox(window_frm,
                                     width=10,
                                     justify='center',
                                     from_=0.00,
                                     to=self.max_capacity,
                                     textvariable=self.capacity_max_var,
                                     increment=self.increment)
        input_capacity_max.grid(row=4, column=1, padx=5, pady=5, stick='w')

        # Unidade de medida
        lbl_measure_ini = tk.Label(window_frm, text='Grandeza:', font=font.Font(size=10, weight='bold'))
        lbl_measure_ini.grid(row=5, column=0, padx=10, pady=5, stick='e')

        self.cbbox_measure_ini = ttk.Combobox(window_frm, width=15, values=self.list_measure)
        self.cbbox_measure_ini.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        self.cbbox_measure_ini.current(measure_ini)

        # Tipo de material do recipiente
        #lbl_container_material_ini = tk.Label(window_frm, text='Material do Recipiente:', font=font.Font(size=10, weight='bold'))
        #lbl_container_material_ini.grid(row=6, column=0, padx=5, pady=5, stick='w')

        #self.cbbox_material_ini = ttk.Combobox(window_frm, values=self.list_container_materials)
        #self.cbbox_material_ini.grid(row=6, column=1, columnspan=3, padx=5, pady=5, sticky='we')
        #if material_ini > -1:
        #    self.cbbox_material_ini.current(material)

        # Conteúdo do galão
        lbl_content_ini = tk.Label(window_frm, text="Conteúdo:", font=font.Font(size=10, weight='bold'))
        lbl_content_ini.grid(row=7, column=0, padx=5, pady=5, stick='w')

        self.cbbox_content_ini = ttk.Combobox(window_frm, values=self.list_contents)
        self.cbbox_content_ini.grid(row=7, column=1, columnspan=3, padx=5, pady=5, sticky='we')
        self.cbbox_content_ini.current(content_ini)

        # Marca
        #lbl_brand_ini = tk.Label(window_frm, text="Marca:", font=font.Font(size=10, weight='bold'))
        #lbl_brand_ini.grid(row=8, column=0, padx=5, pady=5, stick='w')

        #self.cbbox_brand_ini = ttk.Combobox(window_frm, values=self.list_brands)
        #self.cbbox_brand_ini.grid(row=8, column=1, columnspan=3, padx=5, pady=5, sticky='we')
        #if brand_ini > -1:
        #    self.cbbox_brand_ini.current(brand_ini)

        sep = ttk.Separator(window_frm, orient='horizontal')
        sep.grid(row=9, column=0, columnspan=4, padx=5, pady=10, stick='we')

        # Botão
        btn_register = tk.Button(window_frm, text='Criar', font=font.Font(size=10, weight='bold'), command= lambda: (self.create_dump_automatically(), window.destroy()))
        btn_register.configure(bg='#cccccc')
        btn_register.grid(row=10, column=0, columnspan=4, padx=5, pady=5)



    def create_dump_automatically(self):
        # 1ª Verificação - identificação do recipiente.
        if self.registry_ini_var.get() == '':
            tkmsg.showwarning('Aviso','O campo de registro deve ser preenchido')
            self.create_dump_automatically_menu(self.cbbox_container_type_ini.current(), self.registry_ini_var.get(), self.capacity_min_var.get(), self.capacity_max_var.get(), self.cbbox_measure_ini.current(), self.cbbox_content_ini.current())
        else:
            try:
                # 2ª Verificação - quantidade de registros capacidade do recipiente.
                if self.qtd_var.get() <= 0 or self.qtd_var.get() == "" or self.capacity_min_var.get() <= 0.0 or self.capacity_max_var.get() <= 0.0 or self.capacity_max_var.get() <= self.capacity_min_var.get():
                    tkmsg.showwarning('Aviso','A quantidade de registros a serem gerados deve ser preenchida e não pode assumir valor inferior a 1.\n\nAs capacidades devem assumir valor maior que zero.\n\nA capacidade máxima deve assumir valor diferente e maior que a capacidade mínima.')
                    self.create_dump_automatically_menu(self.cbbox_container_type_ini.current(), self.registry_ini_var.get(), self.capacity_min_var.get(), self.capacity_max_var.get(), self.cbbox_measure_ini.current(), self.cbbox_content_ini.current())
                else:
                    for i in range(0,self.qtd_var.get()):
                        #print(i," - reg: ",str(int(self.registry_ini_var.get()) + i) )

                        # 3ª Verificação - duplicidade *** NÃO SERÁ EXECUTADA NESTE BLOCO

                        # Definir o registro
                        registro = str(int(self.registry_ini_var.get()) + i)
                                                
                        # Definir a capacidade
                        capacidade_aleatorio = random.uniform(self.capacity_min_var.get(), self.capacity_max_var.get())
                        capacidade = float("{:.2f}".format(capacidade_aleatorio))
                        
                        container_dumped = Container(capacidade, self.cbbox_container_type_ini.get(), self.cbbox_content_ini.get(), self.cbbox_measure_ini.get(), registro, '', '')

                        self.list_containers_dumped.append(container_dumped)

                        self.lbx_containers_dumped.insert(tk.END, container_dumped.get_info_dict())
            except ValueError as erro:
                tkmsg.showerror('Erro', 'Avisar ao administrador do sistema.\n\nErro:\n'+str(erro))
                self.create_dump_automatically_menu(self.cbbox_container_type_ini.current(), self.registry_ini_var.get(), self.capacity_min_var.get(), self.capacity_max_var.get(), self.cbbox_measure_ini.current(), self.cbbox_content_ini.current())
                

    # Limpar seleção de todos os ListBox
    def clear_lbox_selection(self):
        self.lbx_containers_main.selection_clear(0, tk.END)
        self.lbx_containers_dumped.selection_clear(0, tk.END)

    ## BLOCO EXPORT **************************************************************************************************
    def export_csv(self):
        window = tk.Toplevel(self.root)
        window.wm_title("Exportar *.CSV")
        window.transient(self.root)
        window.grab_set()

        window_frm = tk.Frame(window)
        window_frm.grid(row=0, column=0, padx=10, pady=10, stick='nw')

        lblfrm_tipo = tk.LabelFrame(window_frm, text='Tipo de recipiente')
        lblfrm_tipo.grid(row=0, column=0, columnspan=2, padx=5, pady=5, stick='we')

        tipo_selecionado = tk.StringVar()
        rdbtn_principal = tk.Radiobutton(lblfrm_tipo, text='Principal', variable=tipo_selecionado, value='Principal', tristatevalue=0)
        rdbtn_principal.grid(row=0, column=0, padx=5, pady=5, ipadx=3, ipady=3)

        rdbtn_despejo = tk.Radiobutton(lblfrm_tipo, text='Despejo', variable=tipo_selecionado, value='Despejo', tristatevalue=0)
        rdbtn_despejo.grid(row=1, column=0, padx=5, pady=5, ipadx=3, ipady=3)

        # Método para escolher diretório de salvamento
        def choice_dir():
            file_dir = fdlg.asksaveasfile(
                title="Escolha o diretório de exportação",
                parent=window,
                defaultextension="csv",
                filetypes=(("Arquivo CSV"),("Todos os arquivos","*.*")),
                initialdir=os.getcwd(),
                confirmoverwrite=True,
                initialfile=tipo_selecionado.get()+".csv",
                mode="w")

            arquivo = file_dir.name
            file_dir.close()

            with open(arquivo, 'w', newline='') as arq:
                nome_campos = ['registry', 'type', 'capacity', 'measure', 'content', 'brand', 'material']

                escritor_csv = csv.DictWriter(
                    arq,
                    delimiter=';',
                    dialect='excel',
                    fieldnames=nome_campos,
                    quoting=csv.QUOTE_NONNUMERIC)
                # escreve o cabeçalho
                escritor_csv.writeheader()
                
                if tipo_selecionado.get() == 'Principal':
                    for container in self.list_containers_main:
                        escritor_csv.writerow(container.get_info_dict())
                else:
                    for container in self.list_containers_dumped:
                        #print(container.get_info_dict())
                        escritor_csv.writerow(container.get_info_dict())

        btn_export = tk.Button(window_frm, text='Exportar', font=font.Font(size=10, weight='bold'), command= lambda: (choice_dir(), window.destroy()))
        btn_export.configure(bg='#cccccc')
        btn_export.grid(row=1, column=0, columnspan=2, padx=5, pady=10, stick='we')
        
    ## BLOCO EXPORT **** FIM *****************************************************************************************

    ## BLOCO IMPORT **************************************************************************************************
    def import_csv(self):
        window = tk.Toplevel(self.root)
        window.wm_title("Importar *.CSV")
        window.transient(self.root)
        window.grab_set()

        window_frm = tk.Frame(window)
        window_frm.grid(row=0, column=0, padx=10, pady=10, stick='nw')

        lblfrm_tipo = tk.LabelFrame(window_frm, text='Tipo de recipiente')
        lblfrm_tipo.grid(row=0, column=0, columnspan=2, padx=5, pady=5, stick='we')

        tipo_selecionado = tk.StringVar()
        rdbtn_principal = tk.Radiobutton(lblfrm_tipo, text='Principal', variable=tipo_selecionado, value='Principal', tristatevalue=0)
        rdbtn_principal.grid(row=0, column=0, padx=5, pady=5, ipadx=3, ipady=3)

        rdbtn_despejo = tk.Radiobutton(lblfrm_tipo, text='Despejo', variable=tipo_selecionado, value='Despejo', tristatevalue=0)
        rdbtn_despejo.grid(row=1, column=0, padx=5, pady=5, ipadx=3, ipady=3)

        header_var = tk.IntVar()
        ckbtn_header = tk.Checkbutton(window_frm, text='A 1ª linha é Cabeçalho', variable=header_var)
        ckbtn_header.grid(row=1, column=0, padx=5, pady=5)

        # Método para escolher diretório de salvamento
        def choice_dir():
            file_dir = fdlg.askopenfile(
                title="Escolha o diretório de exportação",
                parent=window,
                defaultextension="csv",
                filetypes=(("Arquivo CSV"),("Todos os arquivos","*.*")),
                initialdir=os.getcwd(),
                initialfile="")

            arquivo = file_dir.name

            file_dir.close()

            with open(arquivo, newline='') as arq:
                nome_campos = ['registry', 'type', 'capacity', 'measure', 'content', 'brand', 'material']

                leitor_csv = csv.DictReader(
                    arq,
                    delimiter=';',
                    fieldnames=nome_campos)

                # Faz com que a primeira linha seja ignorada, ou seja, não será importada. Importante se esta for header (cabeçalho).
                if header_var.get() == 1:
                    next(leitor_csv, None) 

                # No Python versão antes da 8 retorna OrderedDict, após retorna dict
                if tipo_selecionado.get() == 'Principal':
                    self.clear_lbx_containers_main()
                    for linha in leitor_csv:
                        #print(linha['registry'], linha['type'], linha['capacity'], linha['measure'], linha['content'], linha['brand'], linha['material'])
                        container_main = Container(linha['capacity'], linha['type'], linha['content'], linha['measure'], linha['registry'], linha['brand'], linha['material'])

                        self.list_containers_main.append(container_main)

                        self.lbx_containers_main.insert(tk.END, container_main.get_info_dict())
                else:
                    self.clear_lbx_containers_dumped()
                    for linha in leitor_csv:
                        #print(linha['registry'], linha['type'], linha['capacity'], linha['measure'], linha['content'], linha['brand'], linha['material'])
                        container_dumped = Container(linha['capacity'], linha['type'], linha['content'], linha['measure'], linha['registry'], linha['brand'], linha['material'])

                        self.list_containers_dumped.append(container_dumped)

                        self.lbx_containers_dumped.insert(tk.END, container_dumped.get_info_dict())
                    

        ttk.Separator(window_frm, orient='horizontal').grid(row=2, column=0, columnspan=2, padx=5, pady=5, stick='we')
        
        btn_export = tk.Button(window_frm, text='Importar', font=font.Font(size=10, weight='bold'), command= lambda: (choice_dir(), window.destroy()))
        btn_export.configure(bg='#cccccc')
        btn_export.grid(row=3, column=0, columnspan=2, padx=5, pady=10, stick='we')
        
    ## BLOCO IMPORT **** FIM *****************************************************************************************

    ## BLOCO ANÁLISE *************************************************************************************************
    def analysis(self):
        # Limpa o LabelFrame Resultados
        self.clear_frm_resultados()

        # Verifica se foi selecionado um recipiente principal
        if self.index_main_selected > -1:
            # usa o índice do container principal selecionado e obtem seu registro e capacidade (registry e capacity)
            container_obj = self.list_containers_main[self.index_main_selected]   # obtem o objeto da lista
            dict_main = container_obj.get_info_dict()
            #print(type(dict_main['capacity']),' - ', dict_main['capacity']) # Vem com formato str
            registro = dict_main['registry']
            capacidade = float(dict_main['capacity'].replace(',','.'))
            unidade_medida = dict_main['measure']
        
            # organiza informações na lista de despejo [{'index':capacity},...] convertendo volume string para float quando necessário.
            list_container_despejo = []
            for container in self.list_containers_dumped:
                #print(container.get_registry(), ' - ', float(container.get_capacity().replace(',','.')))
                if type(container.get_capacity()) is str:
                    list_container_despejo.append({container.get_registry(): float(container.get_capacity().replace(',','.'))})
                else:
                    list_container_despejo.append({container.get_registry(): container.get_capacity()})

            # Teste dos valores
            #print("Capacidade máxima: ", capacidade)
            #print("Garrafas registradas")
            #for i in range(0,len(list_container_despejo)):
            #    print(list_container_despejo[i])
            #print()
            #print("Teste: verificar list_container_despejo")
            #for registro in list_container_despejo:
            #    for key,value in registro.items():
            #        print(key,' - ', value)
            
            # Instancia objeto do algoritmo e exibe resultados
            analisador = SelectContainers(capacidade, list_container_despejo)
            analisador.execute()

            # Obter o container escolhido no algoritmo
            container_selecionado = analisador.get_selecteds()

            resposta = ''
            if analisador.check_selecteds():
                resposta = '\nVolume máximo: {:.2f}\n'.format(capacidade)
                resposta += '\nConjunto de recipientes selecionados e sobra\n'
                resposta += '[reg1: volume, reg2: volume, ...] - Sobra: volume'
                resposta += '\n\n['
                for key,value in container_selecionado.items():
                    if key == 'lista':
                        for item in value:
                            for k,v in item.items():
                                resposta = ''.join([resposta, k+": "+str(v)+"L, "])
                        resposta = resposta[:-2] +" ]"
                    if key == 'sobra':
                        resposta = '- Sobra: '.join([resposta, '{:.2f}'.format(value)])
            else:
                resposta = '\nOs volume dos recipientes de despejo não será suficiente para encher o recipiente principal.'
            # Exibir resultado na tela
            self.carrega_resultado_input(resposta)

            # Desabilita o recipiente principal selecionado e reinicia a variável tipo "Flag" atribuindo -1
            self.lbx_containers_main.itemconfig(self.index_main_selected, bg='white', fg='black')
            self.index_main_selected = -1

        else:
            tkmsg.showwarning("Aviso", "Favor selecionar um container principal")

    def analysis_selecteds(self):
        # Limpa o LabelFrame Resultados
        self.clear_frm_resultados()
        
        # Verifica se foi selecionado um recipiente principal
        if self.index_main_selected > -1:
            # usa o índice do container principal selecionado e obtem seu registro e capacidade (registry e capacity)
            container_obj = self.list_containers_main[self.index_main_selected]   # obtem o objeto da lista
            dict_main = container_obj.get_info_dict()
            #print(type(dict_main['capacity']),' - ', dict_main['capacity']) # Vem com formato str
            registro = dict_main['registry']
            capacidade = float(dict_main['capacity'].replace(',','.'))
            unidade_medida = dict_main['measure']

            # Obtem na lista os índices dos itens selecionados
            selecao = self.lbx_containers_dumped.curselection()

            
            # organiza informações na lista de dicionários de itens de despejo [{'index':capacity},...] convertendo volume string para float quando necessário.
            list_container_despejo = []
            for indice in selecao:
                container = self.list_containers_dumped[indice]
                #print(container.get_registry(), ' - ',float(container.get_capacity().replace(',','.')))
                if type(container.get_capacity()) is str:
                    list_container_despejo.append({container.get_registry(): float(container.get_capacity().replace(',','.'))})
                else:
                    list_container_despejo.append({container.get_registry(): container.get_capacity()})

            # Instancia objeto do algoritmo e exibe resultados
            analisador = SelectContainers(capacidade, list_container_despejo)
            analisador.empty_container()
            analisador.execute_selecao()


            texto = "Recipiente Principal\n"
            texto += "    Registro: {}\n".format(registro)
            texto += "    Capacidade máxima: {} {}\n".format(capacidade, unidade_medida)
            texto += "\nRecipientes de Despejo Selecionados\n"
            texto += "    Quantidade: {}\n".format(len(analisador.get_selected()))
            texto += "    Volume total: {:.2f} {}\n".format(analisador.get_volume_selected(), unidade_medida)
            texto += "    Sobra: {:.2f} {}\n".format(analisador.get_over(), unidade_medida)
            texto += "    Lista de recipientes:\n"
            for container in analisador.get_selected():
                for key, value in container.items():
                    registry = key
                    volume = value
                    texto += "        Reg: {} - vol: {}\n".format(registry, volume)
            texto += "\n*** Fim **********\n\n"
            
            # carrega input
            self.carrega_resultado_input(texto)

            # Desabilita o recipiente principal selecionado e reinicia a variável tipo "Flag" atribuindo -1
            self.lbx_containers_main.itemconfig(self.index_main_selected, bg='white', fg='black')
            self.index_main_selected = -1
            
        else:
            tkmsg.showwarning("Aviso", "Favor selecionar um container principal")
        
    ## BLOCO ANÁLISE **** FIM ****************************************************************************************

    def clear_frm_resultados(self):

        for widget in self.lblfrm_resultados.winfo_children():
            widget.destroy()

    def carrega_resultado_input(self, texto):
        self.result_scrolled = tkst.ScrolledText(self.lblfrm_resultados, width=50, wrap='word')
        self.result_scrolled.insert("1.0", texto)
        self.result_scrolled.grid(row=0, column=0, columnspan=4, padx=5, pady=5, stick='nwe')

    
def principal(args):
    app_proc = meu_Aplicativo()
    app_proc.execute()
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv))

