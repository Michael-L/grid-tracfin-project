import { Component } from '@angular/core';
import { DesignatedPerson } from '../models/designated-person';

@Component({
  standalone: true,
  selector: 'app-designated-person-editor',
  imports: [],
  templateUrl: './designated-person-editor.component.html',
  styleUrl: './designated-person-editor.component.scss'
})
export class DesignatedPersonEditorComponent {
  designatedPerson: DesignatedPerson = {
    lastname: 'LADOWICHX',
    firstname: 'Michaël'
  }
}
